using System.Globalization;
using System.Text.Json;
using AquaApi;
using Azure.Identity;
using Azure.Storage.Blobs;
using CsvHelper;

var builder = WebApplication.CreateBuilder(args);

// Add services to the container
builder.Services.AddEndpointsApiExplorer();
builder.Services.AddSwaggerGen();

// Register the BlobServiceClient with the connection string from app settings
builder.Services.AddSingleton(x =>
{
    var connectionString = builder.Configuration.GetConnectionString("BlobStorage");
    return new BlobServiceClient(connectionString);
});

var app = builder.Build();

app.UseSwagger();
app.UseSwaggerUI();

app.MapGet("/", () => "AquaApi is running. Navigate to swagger to test.");

// Endpoint to fetch a CSV from Blob Storage, parse it, and return JSON
app.MapGet(
        "/temperature_predictions/latest",
        async (BlobServiceClient blobServiceClient) =>
        {
            var containerClient = blobServiceClient.GetBlobContainerClient("datalake");
            var blobClient = containerClient.GetBlobClient(
                "havvarsel/gold/havtemp-pred-latest.csv"
            );

            // Check if the file exists
            if (!await blobClient.ExistsAsync())
            {
                return Results.NotFound(new { message = "File not found" });
            }

            // Download the CSV file from Blob Storage
            var downloadStream = new MemoryStream();
            await blobClient.DownloadToAsync(downloadStream);
            downloadStream.Position = 0; // Reset the stream position

            // Parse the CSV file using CsvHelper
            using var reader = new StreamReader(downloadStream);
            using var csv = new CsvReader(reader, CultureInfo.InvariantCulture);
            var records = csv.GetRecords<MeasurementRow>().ToList(); // Dynamically read CSV data
            return Results.Ok(records); // Return the JSON data
        }
    )
    .WithName("DownloadCsvAndParseToJson");

app.Run("http://0.0.0.0:80");
