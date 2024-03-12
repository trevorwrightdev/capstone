import Image from 'next/image'
import barGraph from '../../public/bar-graph.png'
import wordCloud from '../../public/word-cloud.png'
import pieChart from '../../public/pie-chart.png'

export default function Data() {
    return (
        <div className='py-32 w-full flex flex-col text-white gap-4 lg:px-64 px-8 items-center'>
            <p className='text-white text-center max-w-[600px] mb-10'>
                The following is a set of diagrams that quantify the effectiveness of certain keywords in Airbnb listing titles.
            </p>
            <div className='flex flex-col items-center gap-2 w-[90%] md:w-[600px]'>
                <Image
                    className='w-full rounded-md'
                    src={barGraph}
                    width={1024}
                    height={768}
                />
                <p className='text-white text-center'>Bar graph with notable words from the dataset</p>
            </div>
            <div className='flex flex-col items-center gap-2 w-[90%] md:w-[600px]'>
                <Image
                    className='w-full rounded-md'
                    src={wordCloud}
                    width={2560}
                    height={1440}
                />
                <p className='text-white text-center'>Word cloud with notable words from the dataset</p>
            </div>
            <div className='flex flex-col items-center gap-2 w-[90%] md:w-[600px]'>
                <Image
                    className='w-full rounded-md'
                    src={pieChart}
                    width={2560}
                    height={1440}
                />
                <p className='text-white text-center'>Pie graph showing the dominance of the top 30% of words in the dataset</p>
            </div>
        </div>
    )
}
