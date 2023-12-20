import Link from "next/link";
// const AUTH_URL = "http://127.0.0.1:5000/authentication";
const OPENID_URL = 'https://steamcommunity.com/openid/login'

const query = {
  'openid.ns': "http://specs.openid.net/auth/2.0",
  'openid.identity': "http://specs.openid.net/auth/2.0/identifier_select",
  'openid.claimed_id': "http://specs.openid.net/auth/2.0/identifier_select",
  'openid.mode': 'checkid_setup',
  'openid.return_to': 'http://127.0.0.1:3000/authorize',
  'openid.realm': 'http://127.0.0.1:3000'
  }

export default function SteamLoginButton(){

  const urlParams = new URLSearchParams(query)
  const AUTH_URL = `${OPENID_URL}?${urlParams}`
  return (
    <Link className="border px-2 py-1 rounded animate-fadeIn" href={AUTH_URL}>Connect to Steam Library</Link>
  )
}