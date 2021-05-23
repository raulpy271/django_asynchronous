

var interval;


function cut_link(link) {
    let max = 30
    if (link.length > max) {
        return link.substring(0, max)
    }
    return link
}


function fetch_languages() {
    return fetch('data')
    .then(response => {
        return response.json()
    })
}


function convert_json_to_html(json) {
    let link_cutted
    let table = `
        <div>
        <table>
        <tr>
            <th> Nome </th>
            <th> Ano </th>
            <th> paradigma </th>
            <th> Site </th>
        </tr>
        <tr>
        <td colspan="4"> <div class="data"> <table>
    `
    for (language of json) {
        link_cutted = cut_link(language.site)
        table += `
            <tr>
                <td> ${language.name} </td>
                <td> ${language.year} </td>
                <td> ${language.paradigm} </td>
                <td> <a href="${language.site}"> ${link_cutted}</a>
                </td>
            </tr>
        `
    }
    table += '</table></div></td></tr></table></div>'
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


