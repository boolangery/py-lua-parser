from luaparser.astnodes import *
from enum import Enum
from libcpp cimport bool
from libcpp.vector cimport vector
from libcpp.stack cimport stack
from libcpp.set cimport set as cset


cdef class Builder:
    cdef object _stream
    cdef int _line_count
    cdef int _right_index

    cdef object _index_stack
    cdef object _right_index_stack

    cdef str text
    cdef int type

    cdef object _expected
    cdef object _comments_index_stack
    cdef object comments

    cdef inline void save(self)

    cdef inline bool success(self)

    cdef inline object failure(self)

    cdef inline failure_save(self)

    cdef bool next_is_rc(self, int type, bool hidden_right=?)

    cdef bool next_is_c(self, int type, bool hidden_right=?)

    cdef bool next_is(self, int type)

    cdef bool next_in_rc(self, types, bool hidden_right=?)

    cdef bool next_in(self, types)

    cdef handle_hidden_left(self)

    cdef handle_hidden_right(self, is_newline=?)

    cdef get_comments(self)

    cdef get_inline_comment(self)

    cdef abort(self)

    cdef parse_chunk(self)

    cdef parse_block(self)

    cdef parse_stat(self)

    cdef parse_ret_stat(self)

    cdef parse_assignment(self)

    cdef parse_var_list(self)

    cdef parse_var(self, is_stat=?)

    cdef parse_tail(self)

    cdef parse_expr_list(self)

    cdef parse_do_block(self)

    cdef parse_while_stat(self)

    cdef parse_repeat_stat(self)

    cdef parse_local(self)

    cdef parse_goto_stat(self)

    cdef parse_if_stat(self)

    cdef parse_elseif_stat(self)

    cdef parse_else_stat(self)

    cdef  parse_for_stat(self)

    cdef parse_function(self)

    cdef parse_names(self)

    cdef parse_func_body(self)

    cdef parse_param_list(self)

    cdef parse_name_list(self)

    cdef parse_label(self)

    cdef parse_callee(self)

    cdef parse_expr(self)

    cdef parse_or_expr(self)

    cdef parse_and_expr(self)

    cdef parse_rel_expr(self)

    cdef parse_concat_expr(self)

    cdef parse_add_expr(self)

    cdef parse_mult_expr(self)

    cdef parse_bitwise_expr(self)

    cdef parse_unary_expr(self)

    cdef parse_pow_expr(self)

    cdef parse_atom(self)

    cdef parse_lua_str(self, lua_str)

    cdef parse_function_literal(self)

    cdef parse_table_constructor(self, render_last_hidden=?)

    cdef parse_field_list(self)

    cdef parse_field(self)

    cdef parse_field_sep(self)
