import Link from "next/link";
import { AUTH_URL } from "../_api/steam-ai";

export default function SteamLoginButton(){
  return (
    <Link className="border px-2 py-1 rounded animate-fadeIn" href={AUTH_URL}>Connect to Steam Library</Link>
  )
}