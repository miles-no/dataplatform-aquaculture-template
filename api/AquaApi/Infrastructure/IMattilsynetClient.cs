using AquaApi.Domain;

namespace AquaApi;

public interface IMattilsynetClient
{
    Task<HttpResponseMessage> PostLiceCount(LiceCount liceCount);
}