using AquaApi.Application;

namespace AquaApi.Tests;

public class MattilsynetServiceTests
{
    [Fact]
    public async Task PostLiceCount_ShouldReturnSuccess()
    {
        // Act
        var client = new MockMattilsynetClient(); 
        var service = new MattilsynetService(client); 
        var result = await service.PostLiceCount();

        // Assert
        Assert.True(result);
    }
}