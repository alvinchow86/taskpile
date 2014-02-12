// global variable ROOT_URL should be set externally!

$(document).ready(function() {

  $("a.collapse_button").click( function() {
    $(this).parents("div..collapsible:first").find("div.inner").slideToggle(200);
  });

  $("div.task_entry").hover( function() {   $(this).addClass("hover"); },
                             function() {$(this).removeClass("hover"); }
                           );
 
    
});


function createTaskFor(username) {

  var inputElem = $("input#new_entry_" + username);
  var entry = inputElem.val();
  inputElem.val("");

  if (entry != "") {
    var data = { task_entry: entry ,
                 assigned_user: username };
    $.post(ROOT_URL + "ajax/ajax_create_task", data, doneCreateTask, "json");
  }

  return false;   


}

// Callback: Inserts new task div for the user's active tasks list
function doneCreateTask(data, textStatus) {
  var divHtml = data.task_html;
  var newDiv = $(divHtml);
  newDiv.hide();

  var parentDiv = $("#taskpile_"+data.assigned_user+" div.active_tasks");

  newDiv.prependTo(parentDiv).slideDown(200);

}

// Function called by button to mark task completed
function completeTask(task_id, assigned_user) {
  
  var data = { task_id: task_id  ,
               assigned_user: assigned_user,
             };
  $.post(ROOT_URL + "ajax/ajax_complete_task", data, doneCompleteTask, "json");

  // Remove task from active tasks
  var taskDiv = $("#active_task_"+task_id);
  taskDiv.find("div.task_entry_content").fadeOut(400, slideUpParent );

  return false;     
           
}

// Mini-callback, slideup parent div and remove
function slideUpParent() {
  $(this).parent().slideUp(200, function() {$(this).remove();} );
  }


// Mini-callback removes self (called back after animation)
function removeMe() {
  $(this).remove();
}

function doneCompleteTask(data, textStatus) {
 
  var divHtml = data.task_html;
  var assigned_user = data.assigned_user;
  var newDiv = $(divHtml);
  newDiv.hide();

  // remove active task
  //$("#task_"+data.task_id).slideUp(200);
  
  // show in completed tasks

  if ( $("#taskpile_"+assigned_user+" div.completed_task").size() >= 6 ) {

    $("#taskpile_"+assigned_user+" div.completed_task:last").slideUp(200, removeMe);
  }


  newDiv.prependTo($("#taskpile_"+assigned_user+" div.completed_tasks_box")).slideDown(200);
}

function markTaskIncomplete(task_id, assigned_user) {
  var data = { task_id: task_id ,
               assigned_user: assigned_user
             };
  $.post(ROOT_URL + "ajax/ajax_mark_task_incomplete", data, doneCreateTask, "json");

  // Hide task from completed list
  var taskDiv = $("#completed_task_"+task_id);
  taskDiv.find("div.task_entry_content").fadeOut(400, slideUpParent );
  //taskDiv.slideUp(400, function() {$(this).remove();} );
 
  return false;

}

