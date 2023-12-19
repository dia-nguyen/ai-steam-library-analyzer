import Link from "next/link";

export default function AnalyzeLibraryButton({steamId}: {steamId: string}){
  return (
    <Link className="border px-2 py-1 rounded animate-fadeIn" href={`/analyze?steamId=${steamId}`}>Give it to me</Link>
  )
}