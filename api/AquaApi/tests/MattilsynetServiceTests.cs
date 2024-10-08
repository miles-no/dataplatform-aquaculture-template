using Xunit;
using Moq;
using System.Net;
using System.Threading.Tasks;


public class MattilsynetServiceTests
{
    [Fact]
    public async Task PostLiceCount_ShouldReturnSuccess()
    {
        // // Arrange
        // var mockHttpClient = new Mock<HttpClient>();
        // mockHttpClient.Setup(m => m.GetAsync(It.IsAny<string>())).ReturnsAsync(new HttpResponseMessage
        // {
        //     StatusCode = HttpStatusCode.OK,
        //     Content = new StringContent("{\"status\": \"success\"}")
        // });

        // var service = new MattilsynetService();

        // Act
        var result = await MattilsynetService.PostLiceCount();

        // Assert
        Assert.True(result.IsSuccessStatusCode);
        Assert.Contains("POST request successful!", await result.Content.ReadAsStringAsync());
    }

}