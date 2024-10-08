using AquaApi.Domain;

namespace AquaApi.Application;

public class MattilsynetService(IMattilsynetClient client)
{
    public async Task<bool> PostLiceCount()
    {
        var liceCount = new LiceCount
        {
            VoksneHunnlus = 11,
            BevegeligeLus = 4,
            FastsittendeLus = 1,
        };
        var response = await client.PostLiceCount(liceCount);
        return response.IsSuccessStatusCode;
    }
}