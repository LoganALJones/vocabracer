import Link from 'next/link';
import React from 'react';

function Header() {
    return (
        <header className='p-5 bg-blue-500'>
            <Link href="/">
            Header
            </Link> 
        </header>
    )
}

export default Header 
