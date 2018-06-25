(function () {
    const deleteButton = document.getElementById('id_delete_button');
    deleteButton.addEventListener('click', handleDelete);

    function handleDelete(e) {
        if (!confirm('Are you sure you want to delete this link?')) {
            return;
        }

        document.getElementById('id_delete').value = 'yes';
        deleteButton.form.submit();
    }
})();
