using Microsoft.Extensions.FileProviders;

var builder = WebApplication.CreateBuilder(args);

builder.Services.AddOpenApi();

var app = builder.Build();

string pathToClientApp = Path.Combine(builder.Environment.ContentRootPath, "ChatAgentAngularApp/dist/ChatAgentAngularApp");

if (app.Environment.IsDevelopment())
{
    app.MapOpenApi();
}

app.UseHttpsRedirection();

app.MapGet("/version", () => "0.0.0")
    .WithName("Version");

app.UseStaticFiles(new StaticFileOptions { FileProvider = new PhysicalFileProvider(pathToClientApp)});
app.MapFallbackToFile(pathToClientApp);

app.Run();