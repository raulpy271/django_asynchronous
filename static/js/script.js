

var interval;


function fetch_languages() {
    return fetch('data')
    .then(response => {
        return response.json()
    })
}


function convert_json_to_html(json) {
    let table = '<div class="data">'
    table += `
        <table>
        <tr>
            <th> Nome </th>
            <th> Ano </th>
            <th> paradigma </th>
            <th> Site </th>
        </tr>
    `
    for (language of json) {
        table += `
            <tr>
                <td> ${language.name} </td>
                <td> ${language.year} </td>
                <td> ${language.paradigm} </td>
                <td> ${language.site} </td>
            </tr>
        `
    }
    table += '</table></div>'
    return table
}


function render_table() {
    fetch_languages()
    .then(json => {
        let table_div = document.querySelector('div.table_div')
        table_div.innerHTML = "Processando dados..."
        if (json.length !== 0) {
            let table = convert_json_to_html(json)
            table_div.innerHTML = table
            clearInterval(interval)
        }
    }).catch(err => {
        console.log(err)
    })
}


function render_table_with_retry() {
    let table_div = document.querySelector('div.table_div')
    table_div.innerHTML = "Tentando conectar com o servidor..."
    interval = setInterval(render_table, 2000)
}


