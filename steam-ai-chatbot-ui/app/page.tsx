"use client";

import { useEffect, useState } from "react";
import SteamLoginButton from "./_components/SteamLoginButton";
import AnalyzeLibraryButton from "./_components/AnalyzeLibraryButton";
import Typewriter from 'typewriter-effect';

/**
 * Home Component
 *
 * This component serves as the main landing page for the application. It welcomes the user
 * with a typewriter effect message and provides an interface to either log in through Steam
 * (using SteamLoginButton) or analyze their Steam library (using AnalyzeLibraryButton) based on
 * whether a Steam ID is stored locally.
 *
 * States:
 *  - steamId (string): Holds the Steam ID retrieved from local storage, if available.
 *  - showButton (boolean): Controls the visibility of the SteamLoginButton or AnalyzeLibraryButton.
 *
 */
export default function Home() {
  const [steamId, setSteamId] = useState<string>("");
  const [showButton, setShowButton] = useState(false)

  useEffect(() => {
    let storedSteamId = localStorage.getItem('steamId')
    if(storedSteamId) setSteamId(storedSteamId)
  }, []);

  setTimeout(()=>{
    setShowButton(true)
  }, 4000)

  const welcomeMessage = "Hello there, gamer! I'm your personal AI assistant, expertly trained in the subtle art of judging video game tastes. But let's be real, it's not just any taste we're talking about here – it's your Steam library I'm going to dive into."

  return (
    <div>
      <div className="mb-5">
        <Typewriter
          onInit={(typewriter) => {
            typewriter.typeString(welcomeMessage)
            typewriter.start();
          }}
          options={{
            delay: 5,
          }}
        />
      </div>
      {showButton && (
        steamId ? <AnalyzeLibraryButton steamId={steamId} /> :<SteamLoginButton/>
      )}

    </div>
  )
}
