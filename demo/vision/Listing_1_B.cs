using System.Net.Http.Headers;
using Newtonsoft.Json;
using Newtonsoft.Json.Linq;

class Program
{
    static async Task Main(string[] args)
    {
        string apiKey = Environment.GetEnvironmentVariable("OPENAI_API_KEY");

        var client = new HttpClient();
        client.DefaultRequestHeaders.Accept.Add(new MediaTypeWithQualityHeaderValue("application/json"));
        client.DefaultRequestHeaders.Authorization = new AuthenticationHeaderValue("Bearer", apiKey);

        var payload = new
        {
            model = "gpt-4o",
            messages = new[]
            {
                new
                {
                    role = "user",
                    content = new object[]
                    {
                        new { type = "text", text = "What do you see in this image?" },
                        new { type = "image_url", image_url = new { url = "https://bit.ly/img_city_1" } }
                    }
                }
            },
            max_tokens = 1000
        };

        var jsonPayload = JsonConvert.SerializeObject(payload);
        var content = new StringContent(jsonPayload, System.Text.Encoding.UTF8, "application/json");

        var response = await client.PostAsync("https://api.openai.com/v1/chat/completions", content);
        var responseString = await response.Content.ReadAsStringAsync();
        var responseData = JsonConvert.DeserializeObject<JObject>(responseString);

        string result = responseData["choices"]?[0]?["message"]?["content"]?.ToString();
        Console.WriteLine(result);
    }
}