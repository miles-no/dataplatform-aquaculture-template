using Microsoft.Azure.Functions.Worker;
using Microsoft.Extensions.Hosting;
using Microsoft.Extensions.DependencyInjection;

var host = new HostBuilder()
    .ConfigureFunctionsWebApplication(
        )
    .ConfigureServices(services =>
    {
        services.AddApplicationInsightsTelemetryWorkerService(); // Optional: App Insights
        services.ConfigureFunctionsApplicationInsights();        // Optional: App Insights config
    })
    .Build();

host.Run();