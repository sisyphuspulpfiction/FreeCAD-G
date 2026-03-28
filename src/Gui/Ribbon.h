// SPDX-License-Identifier: LGPL-2.1-or-later

#pragma once

#include <QWidget>
#include <QTabWidget>
#include <QHBoxLayout>
#include <QToolButton>
#include <QLabel>
#include <QScrollArea>

namespace Gui {

class RibbonGroup : public QWidget {
    Q_OBJECT
public:
    explicit RibbonGroup(const QString& title, QWidget* parent = nullptr);
    void addCommand(const QByteArray& commandName);
    void addSeparator();

private:
    QHBoxLayout* layout;
    QLabel* titleLabel;
};

class RibbonTab : public QWidget {
    Q_OBJECT
public:
    explicit RibbonTab(QWidget* parent = nullptr);
    RibbonGroup* addGroup(const QString& title);

private:
    QHBoxLayout* layout;
};

class Ribbon : public QWidget {
    Q_OBJECT
public:
    explicit Ribbon(QWidget* parent = nullptr);
    RibbonTab* addTab(const QString& title);
    void clear();

private:
    QTabWidget* tabWidget;
};

} // namespace Gui
