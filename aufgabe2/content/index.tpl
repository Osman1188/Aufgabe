<!DOCTYPE html>
<html>

<head>
    <title>Praktikum 2</title>
    <meta charset="UTF-8" />
    <link rel="stylesheet" type="text/css" href="styles.css" />
</head>

<body>
    <div>
        <h1>Ihre Kontakte</h1>
        <div>
            <table class="styled-table">
                <thead>
                    <tr>
                        <th>Vorname</th>
                        <th>Nachname</th>
                        <th>Geburtsdatum</th>
                    </tr>
                </thead>
                <tbody>

                    % for student in students:
                    <tr>
                        <td>${student["Vorname"]}</td>
                        <td>${student["Nachname"]}</td>
                        <td>${student["Geburtsdatum"]}</td>
                    </tr>
                    % endfor
                </tbody>
            </table>
        </div>
    </div>
</body>

</html>
