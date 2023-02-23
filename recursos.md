# Inclusión de recursos

Ejemplo de un fichero *.gitignore*:
```
# Visual Studio Code #
.vscode/

# Mac OS #
# General
.DS_Store
*.icloud

# C #
*.d
*.o
*.a

# Project #
HAL
```


# Versión 0.1.0

## `develop`

```C
int ft_isdigit(char d)
{
	return ('0' <= d && d <= '9');
}
```

```C
int ft_isoperator(char c)
{
	return (c == '+' || c == '-' || c == '*' || c == '/');
}
```

```C
int ft_isspace(char c)
{
	return (c == ' ');
}
```

```C
#include <stdio.h>

char    *in_read(char* str)
{
	char    *expr;
	
	expr = (char*) malloc(3);
	if (!expr)
		return (NULL);
	if (strlen(str) == 5
		&& ft_isdigit(str[0]) && ft_isoperator(str[2]) && ft_isdigit(str[4]))
	{
		expr[0] = str[0];
		expr[1] = str[2];
		expr[2] = str[4];
	}
	else
	{
		printf("Error: bad expression\n");
		return (NULL);
	}
	return (expr);
}
```

## `operations`


```C
int	op_add(int a, int b)
{
	return (a + b);
}
```

```C
int	op_sub(int a, int b)
{
	return (a - b);
}
```

```C
int	op_mul(int a, int b)
{
	return (a * b);
}
```

```C
#include <stdio.h>

int	op_div(int a, int b)
{
	if (b == 0)
	{
		printf("Error: not a number\n");
		return (0);
	}
	return (a / b);
}
```

```C
#ifndef OPERATIONS_H
# define OPERATIONS_H

int		op_add(int a, int b);
int		op_sub(int a, int b);
int		op_mul(int a, int b);
int		op_div(int a, int b);

#endif
```

## `develop`
```C
void	print_help(void)
{
	printf("Usage: ./HAL \"num op num\"\n");
	printf("    where\n");
	printf("        <num> is a number\n");
	printf("        <op> is one of \'+\', \'-\', \'*\', \'/\'\n");
}
```

```C
#include <stdlib.h>
#include <stdio.h>
#include <string.h>
#include "operations.h"

int	main(int argc, char **args)
{
	char	*expr;
	int		a;
	int		b;

	if (argc == 2)
	{
		expr = in_read(args[1]);
		if (!expr)
			return (1);
		a = expr[0] - '0';
		b = expr[2] - '0';
		if (expr[1] == '+')
			printf("%d\n", op_add(a, b));
		else if (expr[1] == '-')
			printf("%d\n", op_sub(a, b));
		else if (expr[1] == '*')
			printf("%d\n", op_mul(a, b));
		else if (expr[1] == '/')
			printf("%d\n", op_div(a, b));
		else
		{
			printf("Error: bad expression\n");
			return (1);
		}
		free(expr);
	}
	else
		printf("Error: bad expression\n");
	return (0);
}
```

```Makefile
### VARIABLES ###

# Names
NAME	= 	HAL

# Instructions
CC 		=	gcc -Wall -Wextra -Werror
RM 		= 	rm -f

# Files
SOURCES = 	$(wildcard *.c)
OBJECTS =	$(SOURCES:.c=.o)


### RULES ###

# Main rules
all: $(OBJECTS)
	@$(CC) -o $(NAME) $(OBJECTS)
	@echo "Calculator '$(NAME)' created."

clean:
	@$(RM) $(OBJECTS)
	@echo "Object files removed."

fclean: clean
	@$(RM) $(NAME)
	@echo "File '$(NAME)' removed."

re: fclean all
	@echo "Project recompiled."

.PHONY: all clean fclean re

%.o: %.c
	@$(CC) -c $< -o $@
	@echo "* File '$<' compiled."
```



# Versión 1.0.0

```C
int	ft_isoperator(char *c)
{
	return (ft_strncmp(c, "+", 1) == 0
		|| ft_strncmp(c, "-", 1) == 0
		|| ft_strncmp(c, "*", 1) == 0
		|| ft_strncmp(c, "/", 1) == 0);
}
```

```C
int	main(int argc, char **args)
{
	char	**expr;
	int		a;
	int		b;

	if (argc == 1)
		print_help();
	else if (argc == 2)
	{
		expr = ft_split(args[1], ' ');
		if (!expr)
			return (1);
		a = ft_atoi(expr[0]);
		b = ft_atoi(expr[2]);
		if (ft_strncmp(expr[1], "+", 1) == 0)
			printf("%d\n", op_add(a, b));
		else if (ft_strncmp(expr[1], "-", 1) == 0)
			printf("%d\n", op_sub(a, b));
		else if (ft_strncmp(expr[1], "*", 1) == 0)
			printf("%d\n", op_mul(a, b));
		else if (ft_strncmp(expr[1], "/", 1) == 0)
			printf("%d\n", op_div(a, b));
		else
		{
			printf("Error: bad expression\n");
			return (1);
		}
		free(expr);
	}
	else
		printf("Error: bad expression\n");
	return (0);
}
```

```Makefile
### VARIABLES ###

# Names
NAME 	= 	HAL

# Instructions
CC 		=	gcc -Wall -Wextra -Werror -ILibft
RM 		= 	rm -f

# Files
SOURCES = 	$(wildcard *.c)
OBJECTS =	$(SOURCES:.c=.o)


### RULES ###

# Main rules
all: libft $(OBJECTS)
	@$(CC) -o $(NAME) $(OBJECTS) Libft/libft.a
	@echo "Calculator '$(NAME)' created."

libft:
	@make -C Libft

clean:
	@$(RM) $(OBJECTS)
	@make -C Libft clean
	@echo "Object files removed."

fclean: clean
	@$(RM) $(NAME)
	@make -C Libft fclean
	@echo "File '$(NAME)' removed."

re: fclean all
	@echo "Project recompiled."

.PHONY: all clean fclean re

%.o: %.c
	@$(CC) -c $< -o $@
	@echo "* File '$<' compiled."
```

# Versión 2.0.0

```C
void	operate(int a, char *op, int b)
{
	if (ft_strncmp(op, "+", 1) == 0)
		printf("%d", a + b);
	else if (ft_strncmp(op, "-", 1) == 0)
		printf("%d", a - b);
	else if (ft_strncmp(op, "*", 1) == 0)
		printf("%d", a * b);
	else if (ft_strncmp(op, "/", 1) == 0)
	{
		if (b != 0)
			printf("%d", a / b);
		else
			printf("Error: not a number");
	}
	else
		printf("Error: bad expression");
}
```

```C
int	main(int argc, char **args)
{
	char	**expr;

	if (argc == 1)
		print_help();
	else if (argc == 2)
	{
		expr = ft_split(args[1], ' ');
		if (!expr)
			return (1);
		if (ft_isoperator(expr[1]))
			operate(ft_atoi(expr[0]), expr[1], ft_atoi(expr[2]));
		else
		{
			printf("Error: bad expression");
			return (1);
		}
		free(expr);
	}
	else
	{
		printf("Error: bad expression");
		return (1);
	}
	return (0);
}
```

