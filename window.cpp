#include "window.h"

#include <QApplication>
#include <QPushButton>

Window::Window(QWidget *parent) : QWidget(parent)
{
	setFixedSize(300, 200);

	m_button = new QPushButton("Hello world!", this);
	m_button->setGeometry(20, 20, 260, 160);

	connect(m_button, SIGNAL (clicked()), QApplication::instance(), SLOT (quit()));
}
