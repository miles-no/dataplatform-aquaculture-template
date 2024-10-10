# Use the SDK image to build the app
FROM mcr.microsoft.com/dotnet/sdk:8.0 AS build
WORKDIR /src

# Copy the project file and restore
COPY *.csproj ./
RUN dotnet restore

# Copy the rest of the application and build
COPY . .
RUN dotnet publish -c Release -o /app

# Use the runtime image to run the app
FROM mcr.microsoft.com/dotnet/aspnet:8.0 AS runtime
WORKDIR /app
COPY --from=build /app .
ENTRYPOINT ["dotnet", "AquaApi.dll"]
