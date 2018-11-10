# Pickachu: The BEST color picker for Vim

**Table of Contents**:

<!-- vim-markdown-toc GFM -->

* [Demo](#demo)
* [Installation](#installation)
	* [Plug](#plug)
	* [Pathogen](#pathogen)
	* [Apt-Vim](#apt-vim)
* [Usage](#usage)
	* [Commands](#commands)
		* [Available Apps](#available-apps)
	* [Keyboard shortcuts](#keyboard-shortcuts)
* [Configuration](#configuration)
	* [Global Variables](#global-variables)
		* [Default App](#default-app)
		* [Default Color Format](#default-color-format)
		* [Default Date Format](#default-date-format)
	* [KDE / Qt5 / Qarma support](#kde--qt5--qarma-support)

<!-- vim-markdown-toc -->

## Demo

[Watch the GIF](https://gfycat.com/AccomplishedTintedJoey)

## Installation

**Notes**: 

- You must have a Vim installation with Python3 support. If you're using NeoVim, you can simply type `pip3 install neovim`.
- You must have Zenity installed on your computer. On most Linux operating systems, this is already installed.
- If you're on a Mac, there may still be hope. [Here is a guide on installing Zenity with Homebrew on Mac](https://brewinstall.org/install-zenity-on-mac-with-brew/)

### Plug

Add this line to your plugin loop:

```
Plug 'DougBeney/pickachu'
```

### Pathogen

```
git clone https://github.com/DougBeney/pickachu.git ~/.vim/bundle/nerdtree
```

### Apt-Vim

```
apt-vim install -y https://github.com/DougBeney/pickachu.git
```

## Usage

### Commands

```
:Pick
```

or...

```
:Pick [app] [optional: format]
```

**Note:** The full command of `:Pick` is `:Pickachu`. Use whatever feels more intuitive for you.

**Note:** By default, `app` is set to `color` and `format` has different defaults depending on what app you choose. See more about defaults and how to change them in the [Configuration](#configuration) section

#### Available Apps

- **color** - The color-picker utility. Default format = `hex`.
- **date** - The date-picker utility. Default format is `%m/%d/%Y`. More about formatting is discussed in the [Configuration](#configuration) section.
- **file** - The file-picker utility. There are no format options for this utility.

### Keyboard shortcuts

By default, there are no keyboard mappings to avoid conflicts with mappings you currently use.

However, here are some ideas:

**Mapping the default color picker to `alt+c`:**

```
map <A-c> :Pickachu<CR>
```

**Mapping the file chooser to `alt+f`:**

```
map <A-f> :Pickachu file<CR>
```

**Mapping the date chooser to `alt+d`:**

```
map <A-d> :Pickachu date<CR>
```

## Configuration

### Global Variables

#### Default App

`let g:pickachu_default_app = "color"`

**Available apps:** See [Available Apps](#available-apps)

#### Default Color Format

`let g:pickachu_default_color_format = "hex"`

**Available color formats are:**

- hex
- rgb
- rgba

#### Default Date Format

`let g:pickachu_default_date_format = "%m/%d/%Y"`

Date formatting is done through [Python datetime](https://docs.python.org/2/library/datetime.html). Below is a table showing different formatting codes you could use.

<table class="docutils" border="1">
		<colgroup>
		<col width="15%">
		<col width="43%">
		<col width="32%">
		<col width="9%">
		</colgroup>
		<thead valign="bottom">
		<tr class="row-odd"><th class="head">Directive</th>
		<th class="head">Meaning</th>
		<th class="head">Example</th>
		<th class="head">Notes</th>
		</tr>
		</thead>
		<tbody valign="top">
		<tr class="row-even"><td><code class="docutils literal"><span class="pre">%a</span></code></td>
		<td>Weekday as locale’s
		abbreviated name.</td>
		<td><div class="first last line-block">
		<div class="line">Sun, Mon, …, Sat
		(en_US);</div>
		<div class="line">So, Mo, …, Sa
		(de_DE)</div>
		</div>
		</td>
		<td>(1)</td>
		</tr>
		<tr class="row-odd"><td><code class="docutils literal"><span class="pre">%A</span></code></td>
		<td>Weekday as locale’s full name.</td>
		<td><div class="first last line-block">
		<div class="line">Sunday, Monday, …,
		Saturday (en_US);</div>
		<div class="line">Sonntag, Montag, …,
		Samstag (de_DE)</div>
		</div>
		</td>
		<td>(1)</td>
		</tr>
		<tr class="row-even"><td><code class="docutils literal"><span class="pre">%w</span></code></td>
		<td>Weekday as a decimal number,
		where 0 is Sunday and 6 is
		Saturday.</td>
		<td>0, 1, …, 6</td>
		<td>&nbsp;</td>
		</tr>
		<tr class="row-odd"><td><code class="docutils literal"><span class="pre">%d</span></code></td>
		<td>Day of the month as a
		zero-padded decimal number.</td>
		<td>01, 02, …, 31</td>
		<td>&nbsp;</td>
		</tr>
		<tr class="row-even"><td><code class="docutils literal"><span class="pre">%b</span></code></td>
		<td>Month as locale’s abbreviated
		name.</td>
		<td><div class="first last line-block">
		<div class="line">Jan, Feb, …, Dec
		(en_US);</div>
		<div class="line">Jan, Feb, …, Dez
		(de_DE)</div>
		</div>
		</td>
		<td>(1)</td>
		</tr>
		<tr class="row-odd"><td><code class="docutils literal"><span class="pre">%B</span></code></td>
		<td>Month as locale’s full name.</td>
		<td><div class="first last line-block">
		<div class="line">January, February,
		…, December (en_US);</div>
		<div class="line">Januar, Februar, …,
		Dezember (de_DE)</div>
		</div>
		</td>
		<td>(1)</td>
		</tr>
		<tr class="row-even"><td><code class="docutils literal"><span class="pre">%m</span></code></td>
		<td>Month as a zero-padded
		decimal number.</td>
		<td>01, 02, …, 12</td>
		<td>&nbsp;</td>
		</tr>
		<tr class="row-odd"><td><code class="docutils literal"><span class="pre">%y</span></code></td>
		<td>Year without century as a
		zero-padded decimal number.</td>
		<td>00, 01, …, 99</td>
		<td>&nbsp;</td>
		</tr>
		<tr class="row-even"><td><code class="docutils literal"><span class="pre">%Y</span></code></td>
		<td>Year with century as a decimal
		number.</td>
		<td>1970, 1988, 2001, 2013</td>
		<td>&nbsp;</td>
		</tr>
		<tr class="row-odd"><td><code class="docutils literal"><span class="pre">%H</span></code></td>
		<td>Hour (24-hour clock) as a
		zero-padded decimal number.</td>
		<td>00, 01, …, 23</td>
		<td>&nbsp;</td>
		</tr>
		<tr class="row-even"><td><code class="docutils literal"><span class="pre">%I</span></code></td>
		<td>Hour (12-hour clock) as a
		zero-padded decimal number.</td>
		<td>01, 02, …, 12</td>
		<td>&nbsp;</td>
		</tr>
		<tr class="row-odd"><td><code class="docutils literal"><span class="pre">%p</span></code></td>
		<td>Locale’s equivalent of either
		AM or PM.</td>
		<td><div class="first last line-block">
		<div class="line">AM, PM (en_US);</div>
		<div class="line">am, pm (de_DE)</div>
		</div>
		</td>
		<td>(1),
		(2)</td>
		</tr>
		<tr class="row-even"><td><code class="docutils literal"><span class="pre">%M</span></code></td>
		<td>Minute as a zero-padded
		decimal number.</td>
		<td>00, 01, …, 59</td>
		<td>&nbsp;</td>
		</tr>
		<tr class="row-odd"><td><code class="docutils literal"><span class="pre">%S</span></code></td>
		<td>Second as a zero-padded
		decimal number.</td>
		<td>00, 01, …, 59</td>
		<td>(3)</td>
		</tr>
		<tr class="row-even"><td><code class="docutils literal"><span class="pre">%f</span></code></td>
		<td>Microsecond as a decimal
		number, zero-padded on the
		left.</td>
		<td>000000, 000001, …,
		999999</td>
		<td>(4)</td>
		</tr>
		<tr class="row-odd"><td><code class="docutils literal"><span class="pre">%z</span></code></td>
		<td>UTC offset in the form +HHMM
		or -HHMM (empty string if the
		the object is naive).</td>
		<td>(empty), +0000, -0400,
		+1030</td>
		<td>(5)</td>
		</tr>
		<tr class="row-even"><td><code class="docutils literal"><span class="pre">%Z</span></code></td>
		<td>Time zone name (empty string
		if the object is naive).</td>
		<td>(empty), UTC, EST, CST</td>
		<td>&nbsp;</td>
		</tr>
		<tr class="row-odd"><td><code class="docutils literal"><span class="pre">%j</span></code></td>
		<td>Day of the year as a
		zero-padded decimal number.</td>
		<td>001, 002, …, 366</td>
		<td>&nbsp;</td>
		</tr>
		<tr class="row-even"><td><code class="docutils literal"><span class="pre">%U</span></code></td>
		<td>Week number of the year
		(Sunday as the first day of
		the week) as a zero padded
		decimal number. All days in a
		new year preceding the first
		Sunday are considered to be in
		week 0.</td>
		<td>00, 01, …, 53</td>
		<td>(6)</td>
		</tr>
		<tr class="row-odd"><td><code class="docutils literal"><span class="pre">%W</span></code></td>
		<td>Week number of the year
		(Monday as the first day of
		the week) as a decimal number.
		All days in a new year
		preceding the first Monday
		are considered to be in
		week 0.</td>
		<td>00, 01, …, 53</td>
		<td>(6)</td>
		</tr>
		<tr class="row-even"><td><code class="docutils literal"><span class="pre">%c</span></code></td>
		<td>Locale’s appropriate date and
		time representation.</td>
		<td><div class="first last line-block">
		<div class="line">Tue Aug 16 21:30:00
		1988 (en_US);</div>
		<div class="line">Di 16 Aug 21:30:00
		1988 (de_DE)</div>
		</div>
		</td>
		<td>(1)</td>
		</tr>
		<tr class="row-odd"><td><code class="docutils literal"><span class="pre">%x</span></code></td>
		<td>Locale’s appropriate date
		representation.</td>
		<td><div class="first last line-block">
		<div class="line">08/16/88 (None);</div>
		<div class="line">08/16/1988 (en_US);</div>
		<div class="line">16.08.1988 (de_DE)</div>
		</div>
		</td>
		<td>(1)</td>
		</tr>
		<tr class="row-even"><td><code class="docutils literal"><span class="pre">%X</span></code></td>
		<td>Locale’s appropriate time
		representation.</td>
		<td><div class="first last line-block">
		<div class="line">21:30:00 (en_US);</div>
		<div class="line">21:30:00 (de_DE)</div>
		</div>
		</td>
		<td>(1)</td>
		</tr>
		<tr class="row-odd"><td><code class="docutils literal"><span class="pre">%%</span></code></td>
		<td>A literal <code class="docutils literal"><span class="pre">'%'</span></code> character.</td>
		<td>%</td>
		<td>&nbsp;</td>
		</tr>
		</tbody>
</table>

### KDE / Qt5 / Qarma support

If you are a KDE and/or would rather use Qt5's color picker, install `qarma`.

After doing so, add the following line to your configuration:

`let g:pickachu_default_command = "qarma"`
