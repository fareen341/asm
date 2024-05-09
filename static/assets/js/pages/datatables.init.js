$(document).ready(function () {
  $("#datatable").DataTable({scrollX: true}),
    $("#datatable-buttons")
      .DataTable({
        scrollX:        false,
        scrollCollapse: false,
        lengthChange: !1,
        buttons: ["copy", "excel", "colvis"],
        
      })
      .buttons()
      .container()
      .appendTo("#datatable-buttons_wrapper .col-md-6:eq(0)");
});

$(document).ready(function() {
  $('#example').DataTable( {
      dom: 'QBfrtip',
      scrollY:500,

      buttons: [
          {
              extend: 'colvis',
              postfixButtons: [ 'colvisRestore' ]
          }
          
          
      ],
      columnDefs: [
          {
              targets: [-1,-2,-3,-4,-5,-6],
              visible: false
          }
      ]
  } );
} );

$(document).ready(function() {
  $('#employee').DataTable( {
      dom: 'QBfrtip',
      scrollY:500,

      buttons: [
          {
              extend: 'colvis',
              postfixButtons: [ 'colvisRestore' ]
          }
          
          
      ],
      columnDefs: [
          {
              targets: [-1,-4,-5,-6],
              visible: false
          }
      ]
  } );
} );

$(document).ready(function() {
    $('#software').DataTable( {
        dom: 'QBfrtip',
        scrollY:500,
  
        buttons: [
            {
                extend: 'colvis',
                postfixButtons: [ 'colvisRestore' ]
            }
            
            
        ],
        columnDefs: [
            {
                targets: [],
                visible: false
            }
        ]
    } );
  } );

  $(document).ready(function() {
    $('#colvis').DataTable( {
        dom: 'QBfrtip',
        scrollY:500,
  
        buttons: [
            {
                extend: 'colvis',
                postfixButtons: [ 'colvisRestore' ]
            }
            
            
        ],
        columnDefs: [
            {
                targets: [],
                visible: false
            }
        ]
    } );
  } );

  
  $(document).ready(function() {
    $('#vendor').DataTable( {
        dom: 'QBfrtip',
        scrollY:500,
  
        buttons: [
            {
                extend: 'colvis',
                postfixButtons: [ 'colvisRestore' ]
            }
            
            
        ],
        columnDefs: [
            {
                targets: [,-4,-3],
                visible: false
            }
        ]
    } );
  } );