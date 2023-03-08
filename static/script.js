<script src="http://ajax.googleapis.com/ajax/libs/jquery/1.11.1/jquery.min.js"></script>
<script  type="text/javascript">
    function approveTask(id) {
        data={id:id,new_value:"APPROVED"}
        $.ajax({
            type:"PUT",
            url:"update_value",

            dataType: 'json',
            contentType: 'application/json',
            data:JSON.stringify(data),
            success:function(data){
                console.log('update')
            },
        });
        console.log('error updating user')
    }
</script>