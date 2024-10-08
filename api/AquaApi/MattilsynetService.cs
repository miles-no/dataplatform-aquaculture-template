using System;
using System.Net.Http;
using System.Text;
using System.Text.Json;
class MattilsynetService
{
    public static async Task<HttpResponseMessage> PostLiceCount()
    {
        using var httpClient = new HttpClient();

        string api_url = "https://example.com/";//"https://lakselusrapportering.fisk-dev.mattilsynet.io/api/v1_2/lakselusrapportering";

        var jsonPayload = new
        {
            lusetelling = new
            {
                voksneHunnlus = 11,
                bevegeligeLus = 4,
                fastsittendeLus = 1,
            }
        };

        string jsonString = JsonSerializer.Serialize(jsonPayload);

        HttpContent content = new StringContent(jsonString, Encoding.UTF8, "application/json");


        HttpResponseMessage response = await httpClient.PostAsync(api_url, content);

        return response;


    }
}