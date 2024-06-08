using Azure;
using Azure.AI.OpenAI;
using static System.Environment;

string endpoint = GetEnvironmentVariable("AZURE_OPENAI_ENDPOINT");
string key = GetEnvironmentVariable("AZURE_OPENAI_API_KEY");

var client = new OpenAIClient(new Uri(endpoint), new AzureKeyCredential(key));

CompletionsOptions completionsOptions = new()
{
    DeploymentName = "gpt-35-turbo-instruct", 
    Prompts = { "Tell me about capital of France" },
};

Response<Completions> completionsResponse = client.GetCompletions(completionsOptions);
Console.WriteLine($"\n{completionsResponse.Value.Choices[0].Text}");