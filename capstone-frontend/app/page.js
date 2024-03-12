'use client'
import wordScores from '../json/word_scores.json'
import { useState } from 'react'

function getWordScore(word) {
    return wordScores[word]
}

export default function Home() {

    const [keyword, setKeyword] = useState('')

    function submit() {

    }

    return (
        <div className='w-full py-44 flex items-center justify-center'>
            <div className='py-16 sm:py-24 lg:py-32'>
                <div className='mx-auto grid max-w-7xl grid-cols-1 gap-10 px-6 lg:grid-cols-12 lg:gap-8 lg:px-8'>
                    <div className='max-w-xl text-3xl font-bold tracking-tight text-white sm:text-4xl lg:col-span-7'>
                        <p className='inline sm:block lg:inline xl:block'>
                            Enter a keyword to analyze.
                        </p>
                    </div>
                    <div className='w-full max-w-md lg:col-span-5 lg:pt-2'>
                        <div className='flex gap-x-4'>
                            <input
                                id='keyword'
                                name='keyword'
                                type='text'
                                autoComplete='off'
                                className='min-w-0 flex-auto rounded-md border-0 bg-white/10 px-3.5 py-2 text-white shadow-sm ring-1 ring-inset ring-white/10 placeholder:text-white/75 focus:ring-2 focus:ring-inset focus:ring-white sm:text-sm sm:leading-6'
                                placeholder='Enter a keyword'
                                value={keyword}
                            />
                            <button
                                type='submit'
                                className='flex-none rounded-md bg-white px-3.5 py-2.5 text-sm font-semibold text-indigo-600 shadow-sm hover:bg-indigo-50 focus-visible:outline focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-white'
                            >
                                Submit
                            </button>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    )
}
