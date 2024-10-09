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
        public void Run([TimerTrigger("*/1 * * * * *")] TimerInfo myTimer)
        {
            Console.WriteLine("Running data generator function");
            _logger.LogInformation($"C# Timer trigger function executed at: {DateTime.Now}");
            
            if (myTimer.ScheduleStatus is not null)
            {
                _logger.LogInformation($"Next timer schedule at: {myTimer.ScheduleStatus.Next}");
            }
        }
    }
}
