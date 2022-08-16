import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED6.Parser.scena_writer_helper import *
try:
    import T4252_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('T4252   ._SN')

# id: 0xFFFF offset: 0x0
@scena.Header('Header')
def Header():
    header = ScenaHeader()
    header.mapName        = 'Grancel'
    header.mapModel       = 'T4252.x'
    header.mapIndex       = 1
    header.bgm            = 17
    header.flags          = 0x0000
    header.entryFunction  = 0xFFFF
    header.importTable    = [0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF]
    header.reserved       = 0
    return header

# id: 0xFFFF offset: 0x64
@scena.EntryPoint('EntryPoint')
def EntryPoint():
    return (
        ScenaEntryPoint(
            dword_00        = 0x00000000,
            dword_04        = 0x00000000,
            dword_08        = 0x00001770,
            word_0C         = 0x0004,
            word_0E         = 0x0000,
            dword_10        = 0,
            dword_14        = 9500,
            dword_18        = -10000,
            dword_1C        = 0,
            dword_20        = 0,
            dword_24        = 0,
            dword_28        = 2800,
            dword_2C        = 262,
            word_30         = 45,
            word_32         = 0,
            word_34         = 360,
            word_36         = 0,
            word_38         = 0,
            word_3A         = 0,
            preInitScena    = 0x0000,
            preInitFunction = 0x0000,
            initScena       = 0x0000,
            initFunction    = 0x0001,
        ),
    )

# id: 0x10000 offset: 0xA8
@scena.ChipData('ChipData')
def ChipData():
    return [
        # (ch, cp)
        ('ED6_DT07/CH02460._CH', 'ED6_DT07/CH02460P._CP'),
        ('ED6_DT07/CH02230._CH', 'ED6_DT07/CH02230P._CP'),
        ('ED6_DT07/CH02240._CH', 'ED6_DT07/CH02240P._CP'),
        ('ED6_DT07/CH01220._CH', 'ED6_DT07/CH01220P._CP'),
        ('ED6_DT07/CH01570._CH', 'ED6_DT07/CH01570P._CP'),
        ('ED6_DT07/CH01560._CH', 'ED6_DT07/CH01560P._CP'),
    ]

# id: 0x10001 offset: 0xDA
@scena.NpcData('NpcData')
def NpcData():
    return (
        ScenaNpcData(
            name                = '赫穆特',
            x                   = -63080,
            z                   = 0,
            y                   = -37950,
            direction           = 260,
            word_0E             = 0,
            dword_10            = 3,
            chipIndex           = 3,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0005,
        ),
        ScenaNpcData(
            name                = '达扬',
            x                   = -61160,
            z                   = 0,
            y                   = -35120,
            direction           = 90,
            word_0E             = 0,
            dword_10            = 4,
            chipIndex           = 4,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0003,
        ),
        ScenaNpcData(
            name                = '托克斯',
            x                   = -67120,
            z                   = 0,
            y                   = -32000,
            direction           = 225,
            word_0E             = 0,
            dword_10            = 5,
            chipIndex           = 5,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0004,
        ),
    )

# id: 0x10002 offset: 0x13A
@scena.MonsterData('MonsterData')
def MonsterData():
    return (
    )

# id: 0x10003 offset: 0x13A
@scena.EventData('EventData')
def EventData():
    return (
    )

# id: 0x10004 offset: 0x13A
@scena.ActorData('ActorData')
def ActorData():
    return (
    )

# id: 0x0000 offset: 0x13A
@scena.Code('Init')
def Init():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C8, 2, 0x642)),
            (Expr.TestScenaFlags, ScenaFlag(0x00C8, 6, 0x646)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_164',
    )

    ChrSetChipByIndex(0x0000, 0)
    ChrSetChipByIndex(0x0001, 1)
    ChrSetChipByIndex(0x0138, 2)
    ChrSetFlags(0x0000, 0x1000)
    ChrSetFlags(0x0001, 0x1000)
    ChrSetFlags(0x0138, 0x1000)

    def _loc_164(): pass

    label('loc_164')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CD, 7, 0x66F)),
            Expr.Return,
        ),
        'loc_178',
    )

    ChrSetFlags(0x0009, 0x0080)
    ChrSetFlags(0x000A, 0x0080)

    Jump('loc_1BB')

    def _loc_178(): pass

    label('loc_178')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CD, 3, 0x66B)),
            Expr.Return,
        ),
        'loc_182',
    )

    Jump('loc_1BB')

    def _loc_182(): pass

    label('loc_182')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C8, 6, 0x646)),
            Expr.Return,
        ),
        'loc_196',
    )

    ChrSetFlags(0x0009, 0x0080)
    ChrSetFlags(0x000A, 0x0080)

    Jump('loc_1BB')

    def _loc_196(): pass

    label('loc_196')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C8, 2, 0x642)),
            Expr.Return,
        ),
        'loc_1AA',
    )

    ChrSetFlags(0x0009, 0x0080)
    ChrSetFlags(0x000A, 0x0080)

    Jump('loc_1BB')

    def _loc_1AA(): pass

    label('loc_1AA')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C8, 0, 0x640)),
            Expr.Return,
        ),
        'loc_1B4',
    )

    Jump('loc_1BB')

    def _loc_1B4(): pass

    label('loc_1B4')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C7, 1, 0x639)),
            Expr.Return,
        ),
        'loc_1BB',
    )

    def _loc_1BB(): pass

    label('loc_1BB')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CD, 7, 0x66F)),
            Expr.Return,
        ),
        'loc_1C5',
    )

    Jump('loc_235')

    def _loc_1C5(): pass

    label('loc_1C5')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CD, 3, 0x66B)),
            Expr.Return,
        ),
        'loc_1D4',
    )

    ChrClearFlags(0x0008, 0x0080)

    Jump('loc_235')

    def _loc_1D4(): pass

    label('loc_1D4')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CB, 2, 0x65A)),
            Expr.Return,
        ),
        'loc_1DE',
    )

    Jump('loc_235')

    def _loc_1DE(): pass

    label('loc_1DE')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C9, 1, 0x649)),
            Expr.Return,
        ),
        'loc_1E8',
    )

    Jump('loc_235')

    def _loc_1E8(): pass

    label('loc_1E8')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C6, 7, 0x637)),
            Expr.Return,
        ),
        'loc_1F2',
    )

    Jump('loc_235')

    def _loc_1F2(): pass

    label('loc_1F2')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C5, 7, 0x62F)),
            Expr.Return,
        ),
        'loc_1FC',
    )

    Jump('loc_235')

    def _loc_1FC(): pass

    label('loc_1FC')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C4, 6, 0x626)),
            Expr.Return,
        ),
        'loc_206',
    )

    Jump('loc_235')

    def _loc_206(): pass

    label('loc_206')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C4, 1, 0x621)),
            Expr.Return,
        ),
        'loc_210',
    )

    Jump('loc_235')

    def _loc_210(): pass

    label('loc_210')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C3, 6, 0x61E)),
            Expr.Return,
        ),
        'loc_21A',
    )

    Jump('loc_235')

    def _loc_21A(): pass

    label('loc_21A')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C3, 1, 0x619)),
            Expr.Return,
        ),
        'loc_224',
    )

    Jump('loc_235')

    def _loc_224(): pass

    label('loc_224')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C2, 0, 0x610)),
            Expr.Return,
        ),
        'loc_22E',
    )

    Jump('loc_235')

    def _loc_22E(): pass

    label('loc_22E')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C1, 0, 0x608)),
            Expr.Return,
        ),
        'loc_235',
    )

    def _loc_235(): pass

    label('loc_235')

    Return()

# id: 0x0001 offset: 0x236
@scena.Code('func_01_236')
def func_01_236():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C8, 4, 0x644)),
            Expr.Return,
        ),
        'loc_246',
    )

    ExecExpressionWithVar(
        0x01,
        (
            (Expr.PushLong, 0x54),
            Expr.Nop,
            Expr.Return,
        ),
    )

    def _loc_246(): pass

    label('loc_246')

    ExecExpressionWithVar(
        0x2B,
        (
            (Expr.PushLong, 0xFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Return()

# id: 0x0002 offset: 0x250
@scena.Code('func_02_250')
def func_02_250():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_265',
    )

    OP_99(0x00FE, 0x00, 0x07, 1500)

    Jump('func_02_250')

    def _loc_265(): pass

    label('loc_265')

    Return()

# id: 0x0003 offset: 0x266
@scena.Code('func_03_266')
def func_03_266():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CD, 7, 0x66F)),
            Expr.Return,
        ),
        'loc_273',
    )

    Jump('loc_364')

    def _loc_273(): pass

    label('loc_273')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CD, 3, 0x66B)),
            Expr.Return,
        ),
        'loc_2BE',
    )

    ChrTalk(
        0x00FE,
        (
            '外出休假的人员\n',
            '终于回到城里了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '现在开始可有的忙了哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_364')

    def _loc_2BE(): pass

    label('loc_2BE')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C8, 6, 0x646)),
            Expr.Return,
        ),
        'loc_2C8',
    )

    Jump('loc_364')

    def _loc_2C8(): pass

    label('loc_2C8')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C8, 2, 0x642)),
            Expr.Return,
        ),
        'loc_2D2',
    )

    Jump('loc_364')

    def _loc_2D2(): pass

    label('loc_2D2')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C8, 0, 0x640)),
            Expr.Return,
        ),
        'loc_2F6',
    )

    ChrTalk(
        0x00FE,
        (
            '呼，今天又要加班了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_364')

    def _loc_2F6(): pass

    label('loc_2F6')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C7, 1, 0x639)),
            Expr.Return,
        ),
        'loc_364',
    )

    ChrTalk(
        0x00FE,
        (
            '唉，不管怎么说，\n',
            '现在的人手是不足以完成任务的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '其他的人\n',
            '都被公爵以休假的名义\n',
            '给赶出城去了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_364(): pass

    label('loc_364')

    TalkEnd(0x00FE)

    Return()

# id: 0x0004 offset: 0x368
@scena.Code('func_04_368')
def func_04_368():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CD, 7, 0x66F)),
            Expr.Return,
        ),
        'loc_375',
    )

    Jump('loc_5D6')

    def _loc_375(): pass

    label('loc_375')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CD, 3, 0x66B)),
            Expr.Return,
        ),
        'loc_3EB',
    )

    ChrTalk(
        0x00FE,
        (
            '呼，政变残留问题的处理\n',
            '和一些手头的工作简直堆积如山。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '今天又只有加班了……\n',
            '在王城里做事太辛苦了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_5D6')

    def _loc_3EB(): pass

    label('loc_3EB')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C8, 6, 0x646)),
            Expr.Return,
        ),
        'loc_3F5',
    )

    Jump('loc_5D6')

    def _loc_3F5(): pass

    label('loc_3F5')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C8, 2, 0x642)),
            Expr.Return,
        ),
        'loc_3FF',
    )

    Jump('loc_5D6')

    def _loc_3FF(): pass

    label('loc_3FF')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C8, 0, 0x640)),
            Expr.Return,
        ),
        'loc_4CE',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 2, 0x2)),
            Expr.Return,
        ),
        'loc_450',
    )

    ChrTalk(
        0x00FE,
        (
            '呜呜……\n',
            '只是想象一下公爵大权在握的样子，\n',
            '就感到一阵寒意。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_4CB')

    def _loc_450(): pass

    label('loc_450')

    SetScenaFlags(ScenaFlag(0x0000, 2, 0x2))

    ChrTalk(
        0x00FE,
        (
            '虽说公爵是女王陛下的代理人，\n',
            '但做出决定性指示的却是情报部。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '如果没有理查德上校的话，\n',
            '还不知道会变成什么样子。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_4CB(): pass

    label('loc_4CB')

    Jump('loc_5D6')

    def _loc_4CE(): pass

    label('loc_4CE')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C7, 1, 0x639)),
            Expr.Return,
        ),
        'loc_5D6',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 2, 0x2)),
            Expr.Return,
        ),
        'loc_550',
    )

    ChrTalk(
        0x00FE,
        (
            '这里是处理利贝尔王国\n',
            '政务的重要办公地点。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '虽然现在女王陛下病了，\n',
            '但仍然接受杜南公爵的指示\n',
            '来执行公务。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_5D6')

    def _loc_550(): pass

    label('loc_550')

    SetScenaFlags(ScenaFlag(0x0000, 2, 0x2))

    ChrTalk(
        0x00FE,
        (
            '这里是行政区域。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '是处理利贝尔王国\n',
            '政务的重要办公地点。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '虽然现在女王陛下病了，\n',
            '但仍然接受杜南公爵的指示\n',
            '来执行公务。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_5D6(): pass

    label('loc_5D6')

    TalkEnd(0x00FE)

    Return()

# id: 0x0005 offset: 0x5DA
@scena.Code('func_05_5DA')
def func_05_5DA():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CD, 3, 0x66B)),
            Expr.Return,
        ),
        'loc_6C1',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Return,
        ),
        'loc_61B',
    )

    ChrTalk(
        0x00FE,
        (
            '唉，我最喜欢的钓鱼\n',
            '看来也暂时没空去了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_6BE')

    def _loc_61B(): pass

    label('loc_61B')

    SetScenaFlags(ScenaFlag(0x0000, 0, 0x0))

    ChrTalk(
        0x00FE,
        (
            '今天开始\n',
            '又要继续工作了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '因为公爵经常无所事事，\n',
            '我还以为可以一直休息了，\n',
            '没想到竟然发生了那么多事……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '这样一来要收拾残局\n',
            '可是要花相当的功夫呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_6BE(): pass

    label('loc_6BE')

    Jump('loc_722')

    def _loc_6C1(): pass

    label('loc_6C1')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CB, 2, 0x65A)),
            Expr.Return,
        ),
        'loc_6CB',
    )

    Jump('loc_722')

    def _loc_6CB(): pass

    label('loc_6CB')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C9, 1, 0x649)),
            Expr.Return,
        ),
        'loc_6D5',
    )

    Jump('loc_722')

    def _loc_6D5(): pass

    label('loc_6D5')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C6, 7, 0x637)),
            Expr.Return,
        ),
        'loc_6DF',
    )

    Jump('loc_722')

    def _loc_6DF(): pass

    label('loc_6DF')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C5, 7, 0x62F)),
            Expr.Return,
        ),
        'loc_6E9',
    )

    Jump('loc_722')

    def _loc_6E9(): pass

    label('loc_6E9')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C4, 6, 0x626)),
            Expr.Return,
        ),
        'loc_6F3',
    )

    Jump('loc_722')

    def _loc_6F3(): pass

    label('loc_6F3')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C4, 1, 0x621)),
            Expr.Return,
        ),
        'loc_6FD',
    )

    Jump('loc_722')

    def _loc_6FD(): pass

    label('loc_6FD')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C3, 6, 0x61E)),
            Expr.Return,
        ),
        'loc_707',
    )

    Jump('loc_722')

    def _loc_707(): pass

    label('loc_707')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C3, 1, 0x619)),
            Expr.Return,
        ),
        'loc_711',
    )

    Jump('loc_722')

    def _loc_711(): pass

    label('loc_711')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C2, 0, 0x610)),
            Expr.Return,
        ),
        'loc_71B',
    )

    Jump('loc_722')

    def _loc_71B(): pass

    label('loc_71B')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C1, 0, 0x608)),
            Expr.Return,
        ),
        'loc_722',
    )

    def _loc_722(): pass

    label('loc_722')

    TalkEnd(0x00FE)

    Return()

def main():
    scena.run(globals())

if __name__ == '__main__':
    Try(main)
