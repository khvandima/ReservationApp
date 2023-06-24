import React from 'react';
import moment from 'moment';
import styled from 'styled-components';



const GridWrapper = styled.div`
    display: grid;
    grid-template-columns: repeat(7, 1fr);
    grid-gap: 1.5px;
    background-color: ${props => props.isHeader ? '#1E1F21' : '#404040'};
    ${props => props.isHeader && 'border-bottom: 1px solid #404040'}
`;

const CellWrapper = styled.div`
    min-width: 140px;
    min-height: ${props => props.isHeader ? 24 : 80}px;
    background-color: ${props => props.isWeekend ? '#272829' : '#1E1F21'};
    color: ${props => props.isCurrentMonth ? '#DDDCDD' : '#555759'}; ;
`;

const RowInCell = styled.div`
    display: flex;
    justify-content: ${props => props.justifyContent ? props.justifyContent : 'flex-start'};
    ${props => props.pr && 'padding-right: 8px'}
`;


const DayWrapper = styled.div`
    height: 33px;
    width: 33px;
    display: flex;
    justify-content: center;
    align-items: center;
    margin: 2px;
`;

const CurrentDay = styled.div`
    height: 100%;
    width: 100%;
    background-color: #F00;
    border-radius: 50%;
    display: flex;
    justify-content: center;
    align-items: center;
`;

 const CalendarGrid = ({startDay, today}) => {
    console.log(today);
    console.log(startDay);

    const day = startDay.clone().subtract(1, 'day');

    const daysArray = [...Array(42)].map(() => day.add(1, 'day').clone());

    const isCurrentDay = (day) => moment().isSame(day, 'day');
    const isCurrentMonth = (day) => today.isSame(day, 'month');

    return (
        <>
            <GridWrapper isHeader>
                {[...Array(7)].map((_,i)=> (
                    <CellWrapper isHeader isCurrentMonth key={i}>
                        <RowInCell
                        justifyContent={'flex-end'}
                        pr
                        >
                        {moment().day(i+1).format('ddd')}
                        </RowInCell>
                    </CellWrapper>
                ))}
            </GridWrapper>
            <GridWrapper>
            {
                daysArray.map((dayItem) => (
                <CellWrapper
                    key={dayItem.format('DDMMYYYY')}
                    isWeekend={dayItem.day() === 6 || dayItem.day() === 0}
                    isCurrentMonth={isCurrentMonth(dayItem)}
                >
                    <RowInCell
                        justifyContent={'flex-end'}
                    >
                        <DayWrapper>
                            {!isCurrentDay(dayItem) && dayItem.format('D')}
                            {isCurrentDay(dayItem) &&<CurrentDay>{dayItem.format('D')}</CurrentDay>}
                        </DayWrapper>
                    </RowInCell>

                </CellWrapper>)
            )}
        </GridWrapper>
        </>

    )
}

export default CalendarGrid;