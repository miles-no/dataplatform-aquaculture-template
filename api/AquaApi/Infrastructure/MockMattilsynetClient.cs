using System.Net;
using AquaApi.Domain;

namespace AquaApi;

public class MockMattilsynetClient : IMattilsynetClient
{
    public async Task<HttpResponseMessage> PostLiceCount(LiceCount liceCount)
    {
        await Task.Delay(200);
        return new HttpResponseMessage(HttpStatusCode.Created);
    }
}