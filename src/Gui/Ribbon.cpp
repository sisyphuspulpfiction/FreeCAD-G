// SPDX-License-Identifier: LGPL-2.1-or-later

#include "Ribbon.h"
#include "Application.h"
#include "Command.h"
#include "Action.h"
#include <QVBoxLayout>
#include <QToolButton>
#include <QStyle>
#include <QFrame>

namespace Gui {

RibbonGroup::RibbonGroup(const QString& title, QWidget* parent)
    : QWidget(parent)
{
    QVBoxLayout* mainLayout = new QVBoxLayout(this);
    mainLayout->setContentsMargins(5, 5, 5, 2);
    mainLayout->setSpacing(2);

    QWidget* topWidget = new QWidget(this);
    layout = new QHBoxLayout(topWidget);
    layout->setContentsMargins(0, 0, 0, 0);
    layout->setSpacing(4);

    mainLayout->addWidget(topWidget);

    titleLabel = new QLabel(title, this);
    titleLabel->setAlignment(Qt::AlignCenter);
    titleLabel->setStyleSheet("font-size: 10px; color: #666;");
    mainLayout->addWidget(titleLabel);

    QFrame* line = new QFrame(this);
    line->setFrameShape(QFrame::VLine);
    line->setFrameShadow(QFrame::Sunken);
    line->setStyleSheet("border: 1px solid #ddd;");
}

void RibbonGroup::addCommand(const QByteArray& commandName) {
    Command* cmd = Application::Instance->commandManager().getCommandByName(commandName.constData());
    if (cmd) {
        QToolButton* btn = new QToolButton(this);
        btn->setDefaultAction(cmd->getAction());
        btn->setToolButtonStyle(Qt::ToolButtonTextUnderIcon);
        btn->setIconSize(QSize(32, 32));
        layout->addWidget(btn);
    }
}

void RibbonGroup::addSeparator() {
    QFrame* line = new QFrame(this);
    line->setFrameShape(QFrame::VLine);
    line->setFrameShadow(QFrame::Sunken);
    layout->addWidget(line);
}

RibbonTab::RibbonTab(QWidget* parent)
    : QWidget(parent)
{
    layout = new QHBoxLayout(this);
    layout->setContentsMargins(5, 5, 5, 5);
    layout->setSpacing(10);
    layout->setAlignment(Qt::AlignLeft);
}

RibbonGroup* RibbonTab::addGroup(const QString& title) {
    RibbonGroup* group = new RibbonGroup(title, this);
    layout->addWidget(group);
    return group;
}

Ribbon::Ribbon(QWidget* parent)
    : QWidget(parent)
{
    QVBoxLayout* mainLayout = new QVBoxLayout(this);
    mainLayout->setContentsMargins(0, 0, 0, 0);

    tabWidget = new QTabWidget(this);
    tabWidget->setStyleSheet("QTabWidget::pane { border-top: 1px solid #ddd; }");
    mainLayout->addWidget(tabWidget);

    setFixedHeight(140);
}

RibbonTab* Ribbon::addTab(const QString& title) {
    RibbonTab* tab = new RibbonTab(tabWidget);
    tabWidget->addTab(tab, title);
    return tab;
}

void Ribbon::clear() {
    while (tabWidget->count() > 0) {
        QWidget* tab = tabWidget->widget(0);
        tabWidget->removeTab(0);
        delete tab;
    }
}

} // namespace Gui
