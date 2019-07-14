$(function(){
    var specialElementHandlers = {
        '#editor': function (element, renderer){
            return true
        }
    };

    $('#export_pdf').click(function () {
        var doc = new jsPDF();
        doc.fromHTML($('#invoice').html(), 15, 15, {
            "width": 170,
            "elementHandlers": specialElementHandlers
        });
        doc.save("sb_finance.pdf");
    });
});