"use client";
import { useState, useEffect } from "react";
import { useSearchParams } from 'next/navigation';
import { redirect } from 'next/navigation';

/**
 * Authorize Component
 *
 * This component handles the authorization process for Steam users. It retrieves the Steam ID
 * from the URL query parameters, stores it in local storage, and then redirects the user to
 * the analyze page with the Steam ID as a query parameter
 *
 * The component utilizes two hooks:
 *  - `useSearchParams` from 'next/navigation' to access URL query parameters.
 *  - `useEffect` to handle the side effects of authorization, such as extracting the Steam ID,
 *    storing it in local storage, and performing the redirection.
 *
 * States:
 *  - `steamId` (string): The Steam ID extracted from the URL query parameter 'openid.claimed_id'.
 *
 * Behavior:
 *  - On component mount, the Steam ID is extracted from the URL query parameter 'openid.claimed_id'.
 *  - The Steam ID is then stored in local storage for persistent access across the application.
 *  - The user is redirected to the '/analyze' page, passing the Steam ID as a query parameter.
 *  - Displays a message with the Steam ID if available, otherwise shows an "Authorizing..." message.

 */
export default function Authorize() {
  const [steamId, setSteamId] = useState<string>("");
  const searchParams = useSearchParams();

  useEffect(() => {
    // Fetch the Steam ID from the query parameters
    const claimedId = searchParams.get('openid.claimed_id');
    const steamId = String(claimedId?.split("/").slice(-1));

    if (steamId) {
      setSteamId(steamId);
      // Store the steamId in local storage for future use
      localStorage.setItem('steamId', steamId);


      redirect(`/analyze?steamId=${steamId}`)
    }
  }, [searchParams]);

  return (
    <div>
      {steamId ? (
        <p>Steam ID: {steamId}</p>
      ) : (
        <p>Authorizing...</p>
      )}
    </div>
  );
}
