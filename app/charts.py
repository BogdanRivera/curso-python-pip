import matplotlib.pyplot as plt


def generate_bar_chart(name, labels, values):
    fig, ax = plt.subplots()
    ax.bar(labels, values)
    plt.savefig(f'imgs/{name}Bar.png')
    print(f"La ruta es imgs/{name}Bar.png")
    plt.close()


def generate_pie_chart(labels, values):
    fig, ax = plt.subplots()
    ax.pie(values, labels=labels)
    ax.axis('equal')
    plt.savefig('imgs/Pie.png')


if __name__ == '__main__':
    labels = ['a', 'b', 'c']
    values = [10, 40, 800]
    # generate_bar_chart(labels, values)
