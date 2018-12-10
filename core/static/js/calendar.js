  $(function() {
  $('#calendar').fullCalendar({
    defaultView: 'agendaWeek',
    allDaySlot: false,
    weekends: false,
    minTime: "07:00:00",
    maxTime: "20:00:00",
    header: {
        right: 'month, agendaWeek, agendaDay, prev, next'
         },
    selectable: true,
    dayClick: function (fechaCita) {
        console.log(fechaCita)
        // en fechaCita esta la info
        //Tue Dec 11 2018 08:00:00 GMT+0000
    },
    select: function(start,end){
    var ans = window.confirm("Fecha de cita: " + start.format('DD/MMMM/YYYY') + "\nHorario: " + start.format('h:mm') + " a " + end.format('h:mm'));
    if (ans==true){
            var title= "Ocupado";
            $('#calendar').fullCalendar('renderEvent', {
                title:title,
                start:start,
                end:end,
            },true);
            window.alert('Cita creada.');
        } else{
            window.alert('Cita cancelada.');
        }
    },


  })
  /*$('#calendar').fullCalendar('renderEvent', eventData, true);*/

});