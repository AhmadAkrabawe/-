import tkinter as tk
from tkinter import Text

def paste_and_process():
    # لصق النص من الحافظة
    input_text = root.clipboard_get()
    input_box.delete("1.0", tk.END)
    input_box.insert(tk.END, input_text)

    # معالجة النص
    input_text = input_box.get("1.0", tk.END).strip()

    # الحروف التي سيتم إزالتها
    char = ["َ", "ُ", "ِ", "ُ", "ْ", "ٌ", "ٍ", "ّ", ":"]
    for c in char:
        input_text = input_text.replace(c, "")

    # الحروف التي سيتم استبدالها بأسطر جديدة
    char2 = ["،","."]
    for c in char2:
        input_text = input_text.replace(c, "\n")

    # الكلمات التي سيتم حذفها
    words_to_remove = [
        "عن", "حدثنا", "أخبرنا", "أن ", "أنه ", "يخبر", "قال", "أخبرني", "قالا",
        "يحدث", "سمع", "نا ", "ثنا", "أنا ", "أنبأنا", "أنبأني", "سمعت", "نبأنا",
        "نبأني", "أنبا", "نبا", "قالوا", "جميعا", "حدثني", "قالت",
        "وعن", "وحدثنا", "وأخبرنا", "وأن ", "وأنه", "ويخبر", "وقال", "وأخبرني", "وقالا",
        "ويحدث", "وسمع", "ونا", "وثنا", "وأنا", "وأنبأنا", "وأنبأني", "وسمعت", "ونبأنا",
        "ونبأني", "وأنبا", "ونبا"
    ]

    # حذف الكلمات غير المرغوب فيها
    words = input_text.split(" ")
    for word in words_to_remove:
        input_text = input_text.replace(word, "")

    # تقسيم النص إلى أسطر وإضافة علامات التبويب
    lines = input_text.split("\n")
    lines = [line.strip() for line in lines]
    lines_with_tabs = [("\t" * index) + line for index, line in enumerate(lines, start=0)]

    # النص النهائي
    output_text = "\n".join(lines_with_tabs)

    # عرض النص الناتج
    output_box.delete("1.0", tk.END)
    output_box.insert(tk.END, output_text.strip())

def copy_output():
    output_text = output_box.get("1.0", tk.END).strip()
    root.clipboard_clear()
    root.clipboard_append(output_text)
    root.update()  # تحديث الحافظة

# إنشاء نافذة التطبيق
root = tk.Tk()
root.title("معالجة الإسناد")

# عناصر الواجهة
input_label = tk.Label(root, text="النص المدخل:")
input_label.pack()

input_box = Text(root, height=10, width=50)
input_box.pack()

# زر لصق النص ومعالجته
paste_process_button = tk.Button(root, text="لصق ومعالجة النص", command=paste_and_process)
paste_process_button.pack()

output_label = tk.Label(root, text="النص الناتج:")
output_label.pack()

output_box = Text(root, height=10, width=50, state=tk.NORMAL)
output_box.pack()

# زر نسخ النص الناتج
copy_output_button = tk.Button(root, text="نسخ النص الناتج", command=copy_output)
copy_output_button.pack()


# تشغيل التطبيق
root.mainloop()
