import type { Metadata } from 'next'
import { Inter } from 'next/font/google'
import './globals.css'

const inter = Inter({ subsets: ['latin'] })

export const metadata: Metadata = {
  title: 'Steam AI Library Analyzer',
  description: 'Chat GPT 4 & Steam Web API',
}

export default function RootLayout({
  children,
}: {
  children: React.ReactNode
}) {
  return (
    <html lang="en">
      <body className={inter.className}>
        <main className='container pt-10 max-w-2xl m-auto'>
          {children}
        </main>
      </body>
    </html>
  )
}
