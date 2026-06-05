Get-ChildItem -Recurse -Filter *.py | ForEach-Object {
    manim -qh $_.FullName --save_sections -r 1920,1080
}