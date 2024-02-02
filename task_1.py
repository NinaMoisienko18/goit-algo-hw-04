from pathlib import Path

with open("salary_file.txt", "w") as sf:
    text = "Alex Korp,3000\n" \
           "Nikita Borisenko,2000\n" \
           "Sitarama Raju,1000"
    sf.write(text)


file_name = "salary_file.txt"
path = Path(file_name).absolute()


def total_salary(path):

    try:
        with open(path, "r", encoding="utf-8") as st_read:
            lines = [st.strip() for st in st_read.readlines()]

        total = 0
        count_of_developers = 0
        for line in lines:
            name, salary = line.split(',')
            if total and count_of_developers == 0:
                total = int(salary)
                count_of_developers = 1
            else:
                total += int(salary)
                count_of_developers += 1

            print(f"Ім'я розробника: {name}, ЗП: {salary}$")

        average = total // count_of_developers
        return total, average

    except FileNotFoundError:
        return f">>> Файлу - {path.name} - не існує."




try:
    total, average = total_salary(path)
    print(f"\nЗагальна сума заробітної плати: {total}$, Середня заробітна плата: {average}$")
    path.unlink()

except ValueError as error:
    print(total_salary(path))