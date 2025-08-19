
const templateType = document.getElementById('id_template_type');
const formGroupAll = document.querySelectorAll('.form__group, .form__group-checkbox')

const otherGroups = Array.from(formGroupAll).slice(1)

const toggleFields = () => {
  if(templateType.value === "") {
    otherGroups.forEach(group => {
      group.querySelectorAll('input, select, textarea').forEach(field => {
        field.setAttribute("disabled", "disabled");
        field.classList.add('disabled');
      })
    })
  }else {
    otherGroups.forEach(group => {

      group.querySelectorAll('input, textarea, select').forEach(field => {
        field.removeAttribute("disabled", "disabled");
        field.classList.remove('disabled');
      })
    })

    document.querySelectorAll('.banquet, .funeral, .default')
      .forEach(field => field.classList.remove('active'));
    const templateName = templateType.value;

    const templateFields = document.querySelectorAll(`.${templateName}`);

    templateFields.forEach(field => {
      field.classList.add('active');
    })
  }
}

toggleFields()

templateType.addEventListener('change', toggleFields)
