    select: function(start,end,title){
    var title= "Ocupado";
    var start = $.fullCalendar.moment(start).format();
    var end = $.fullCalendar.moment(end).format();
    },
    eventData: {
        title:title,
        start:start,
        end:end,
    }


//dentro del if
