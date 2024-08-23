
export function normalizeDate(info) {
    let splittedDate = info.split("T", 2);
    let date = splittedDate[0];
    let hour = splittedDate[1].substr(0,5);
    date = date.split('-', 3);
    date = `${date[2]}/${date[1]}/${date[0]}`;

    return { date: date, hour: hour};
}