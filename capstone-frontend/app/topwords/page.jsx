import words from '../../json/sorted_scores.json'

export default function TopWords() {
    return (
        <div className='py-32 w-full flex flex-col text-white gap-4 lg:px-64 px-8 items-center'>
            <h1 className='text-xl md:text-2xl text-center font-bold'>
                Best words and phrases to use in your Airbnb listing title
            </h1>
            {words
                .slice()
                .reverse()
                .map((word, i) => {
                    let color = {
                        color: 'white',
                    }

                    if (word['score'] > 7) {
                        color = {
                            color: '#24ff41',
                        }
                    } else if (word['score'] > 5) {
                        color = {
                            color: 'yellow',
                        }
                    } else if (word['score'] > 3) {
                        color = {
                            color: 'orange',
                        }
                    } else {
                        color = {
                            color: 'red',
                        }
                    }

                    let wordName = word['word']

                    if (wordName === 'cleaning') {
                        wordName = 'no cleaning fee'
                    } else if (wordName === 'entry') {
                        wordName = 'private entry'
                    }

                    return (
                        <div key={i} className='flex justify-between'>
                            <p>
                                <span className='text-black'>{i + 1}</span> {wordName}:{' '}
                                <span style={color}>{word['score']}</span>
                            </p>
                        </div>
                    )
                })}
        </div>
    )
}
