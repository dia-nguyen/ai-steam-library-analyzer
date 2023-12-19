'use client';

import { analyzeSteamLibrary } from '../_api/steam-ai';
import { useState,useEffect, useRef } from 'react';
import { useSearchParams } from 'next/navigation';
import Typewriter from 'typewriter-effect';
import { SteamAnalyzeDataProps } from '../_types/analyze';

/**
 * Analyze Component
 *
 * This component is responsible for analyzing a user's Steam library. It fetches analysis
 * data based on the provided Steam ID and displays the results using a typewriter effect.
 *
 * The component utilizes two primary hooks:
 *  - `useSearchParams` to retrieve the Steam ID from the URL query parameters.
 *  - `useEffect` to fetch data from the Steam analysis API and to control the typewriter effect.
 *
 * States:
 *  - `data` (SteamAnalyzeDataProps): Holds the analysis data fetched from the API. Initialized
 *    with an empty message string.
 *  - `steamId` (string): Extracted from URL query parameters to identify the user's Steam ID.
 *
 * External Libraries:
 *  - `typewriter-effect`: Used for displaying analysis in a typewriter fashion
 *
 */
export default function Analyze(){
  const searchParams = useSearchParams();
  const [data, setData] = useState<SteamAnalyzeDataProps>({message: ""});
  const typewriterRef = useRef<any>(null);

  const steamId = searchParams.get('steamId');

  useEffect(()=> {
    async function fetchData() {
      const result = await analyzeSteamLibrary(steamId);
      setData(result);
    }
    fetchData();
  }, [steamId])

  useEffect(() => {
    if (data && typewriterRef.current) {
      typewriterRef.current
        .typeString(`> <span class='whitespace-pre-wrap leading-5'>${data.message}</span>`)
        .start();
    }
  }, [data]);

    return(
      <div className="inline">
      <Typewriter
        onInit={(typewriter) => {
          typewriterRef.current = typewriter;
          typewriter.typeString("> <span class='leading-5'>Give me a sec</span> <br><br>")
          .pauseFor(500)
          typewriter.typeString("> <span class='leading-5'>Wow, there's a lot of ... stuff happening here</span> <br><br>")
          .pauseFor(500)
          typewriter.typeString("> <span class='leading-5'>Are you ... like .. okay? </span> <br><br>")
          typewriter.typeString("> <span class='leading-5'>Just checking </span> <br><br>")
          .pauseFor(500)
          typewriter.start();
        }}
        options={{
          delay: 5,
        }}
      />
      </div>
    )
  // }
}
