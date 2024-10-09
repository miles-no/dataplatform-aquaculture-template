using System;
using System.Text.Json;
using Microsoft.Azure.Functions.Worker;
using Microsoft.Extensions.Logging;

namespace DataGeneratorFunction
{
    public class DataGeneratorFunction
    {
        private readonly ILogger _logger;

        public DataGeneratorFunction(ILoggerFactory loggerFactory)
        {
            _logger = loggerFactory.CreateLogger<DataGeneratorFunction>();
        }

        [Function("DataGeneratorFunction")]
        [EventHubOutput("dev-aquaplatform-eventhub", Connection = "EventHubConnectionString")]
        public string Run([TimerTrigger("*/1 * * * * *")] TimerInfo myTimer)
        {
            _logger.LogInformation($"C# Timer trigger function executed at: {DateTime.Now}");

            if (myTimer.ScheduleStatus is not null)
            {
                _logger.LogInformation($"Next timer schedule at: {myTimer.ScheduleStatus.Next}");
            }

            // Generate random data
            var randomData = new
            {
                Id = Guid.NewGuid(),
                Timestamp = DateTime.UtcNow,
                Value = new Random().Next(1, 100)
            };

            // Convert data to JSON
            var eventHubMessage = JsonSerializer.Serialize(randomData);

            // Log generated data
            _logger.LogInformation($"Generated data: {eventHubMessage}");
            return eventHubMessage;
        }
    }
}