namespace AquaApi;

public class MeasurementRow
{
    public string lat { get; set; }
    public string lon { get; set; }
    public string variable_name { get; set; }
    public string time { get; set; }
    public string ocean_temperature { get; set; }
    public string depth_meters { get; set; }
    public string fetch_timestamp{ get; set; }
}
