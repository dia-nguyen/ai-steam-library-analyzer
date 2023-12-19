const API_URL = "http://127.0.0.1:5001/analyze";
export const AUTH_URL = "http://127.0.0.1:5000/authentication";
import { AnalyzeSteamLibraryProps } from "../_types/analyze";

export async function analyzeSteamLibrary(steamId: string): Promise<AnalyzeSteamLibraryProps> {
  try {
    const response = await fetch(API_URL, {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({ "steam_id": steamId }), // Include the steamId in the request body
    });

    const result = await response.json();
    return result;

  } catch (error) {
    console.error("Error", error);
  }
}
