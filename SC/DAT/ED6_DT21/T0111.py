import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED62.Parser.scena_writer_helper import *
try:
    import T0111_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('T0111   ._SN')

# id: 0xFFFF offset: 0x0
@scena.Header('Header')
def Header():
    header = ScenaHeader()
    header.mapName        = 'Rolent'
    header.mapModel       = 'T0111.x'
    header.mapIndex       = 11
    header.bgm            = 10
    header.flags          = 0x0000
    header.entryFunction  = 0xFFFF
    header.importTable    = [0xFFFFFFFF, 'ED6_DT21/T0111_1._SN', 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF]
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
        ('ED6_DT07/CH01000._CH', 'ED6_DT07/CH01000P._CP'),
        ('ED6_DT07/CH01030._CH', 'ED6_DT07/CH01030P._CP'),
        ('ED6_DT07/CH01040._CH', 'ED6_DT07/CH01040P._CP'),
        ('ED6_DT07/CH01020._CH', 'ED6_DT07/CH01020P._CP'),
        ('ED6_DT07/CH01170._CH', 'ED6_DT07/CH01170P._CP'),
        ('ED6_DT07/CH01130._CH', 'ED6_DT07/CH01130P._CP'),
        ('ED6_DT07/CH01070._CH', 'ED6_DT07/CH01070P._CP'),
        ('ED6_DT07/CH01530._CH', 'ED6_DT07/CH01530P._CP'),
        ('ED6_DT26/CH20330._CH', 'ED6_DT26/CH20330P._CP'),
    ]

# id: 0x10001 offset: 0xF2
@scena.NpcData('NpcData')
def NpcData():
    return (
        ScenaNpcData(
            name                = '拉欧老人',
            x                   = -35400,
            z                   = 0,
            y                   = 36030,
            direction           = 90,
            word_0E             = 0,
            dword_10            = 0,
            chipIndex           = 0,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0006,
        ),
        ScenaNpcData(
            name                = '亚尔丽 ',
            x                   = -39940,
            z                   = 0,
            y                   = 33130,
            direction           = 135,
            word_0E             = 0,
            dword_10            = 1,
            chipIndex           = 1,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0008,
        ),
        ScenaNpcData(
            name                = '胡里奥',
            x                   = -42500,
            z                   = 0,
            y                   = 37200,
            direction           = 90,
            word_0E             = 0,
            dword_10            = 2,
            chipIndex           = 2,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0007,
        ),
        ScenaNpcData(
            name                = '菲特 ',
            x                   = 37070,
            z                   = 0,
            y                   = 33560,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 3,
            chipIndex           = 3,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0004,
        ),
        ScenaNpcData(
            name                = '尤妮',
            x                   = 38800,
            z                   = 0,
            y                   = 30060,
            direction           = 90,
            word_0E             = 0,
            dword_10            = 4,
            chipIndex           = 4,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0005,
        ),
        ScenaNpcData(
            name                = '芙莉莎',
            x                   = -4550,
            z                   = 0,
            y                   = 37480,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 5,
            chipIndex           = 5,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x000A,
        ),
        ScenaNpcData(
            name                = '阿妮娅',
            x                   = 3140,
            z                   = 0,
            y                   = 32100,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 6,
            chipIndex           = 6,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0003,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x000B,
        ),
        ScenaNpcData(
            name                = '加通老大',
            x                   = 4600,
            z                   = 0,
            y                   = 31530,
            direction           = 90,
            word_0E             = 0,
            dword_10            = 7,
            chipIndex           = 7,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0009,
        ),
    )

# id: 0x10002 offset: 0x1F2
@scena.MonsterData('MonsterData')
def MonsterData():
    return (
    )

# id: 0x10003 offset: 0x1F2
@scena.EventData('EventData')
def EventData():
    return (
    )

# id: 0x10004 offset: 0x1F2
@scena.ActorData('ActorData')
def ActorData():
    return (
    )

# id: 0x0000 offset: 0x1F2
@scena.Code('Init')
def Init():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 0, 0x2000)),
            Expr.Return,
        ),
        'loc_24D',
    )

    ChrSetFlags(0x000F, 0x0080)
    ChrSetFlags(0x0009, 0x0080)
    ChrSetPos(0x0008, -39720, 0, 35090, 0)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0410, 5, 0x2085)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_24A',
    )

    ChrSetFlags(0x000B, 0x0080)
    ChrSetPos(0x000D, 5460, 0, 34000, 90)
    ChrSetPos(0x000E, 2390, 0, 31560, 51)
    CreateThread(0x000E, 0x00, 0x00, func_02_35D)

    def _loc_24A(): pass

    label('loc_24A')

    Jump('loc_306')

    def _loc_24D(): pass

    label('loc_24D')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0340, 0, 0x1A00)),
            Expr.Return,
        ),
        'loc_28C',
    )

    ChrSetFlags(0x0008, 0x0080)
    ChrSetPos(0x000C, 37990, 0, 33540, 315)

    If(
        (
            (Expr.Eval, "OP_29(0x0077, 0x00, 0x10)"),
            Expr.Return,
        ),
        'loc_279',
    )

    ChrSetFlags(0x000F, 0x0080)

    def _loc_279(): pass

    label('loc_279')

    If(
        (
            (Expr.Eval, "OP_29(0x0077, 0x00, 0x04)"),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_289',
    )

    ChrSetFlags(0x000F, 0x0010)

    def _loc_289(): pass

    label('loc_289')

    Jump('loc_306')

    def _loc_28C(): pass

    label('loc_28C')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0304, 2, 0x1822)),
            Expr.Return,
        ),
        'loc_2BA',
    )

    ChrSetPos(0x0008, -41180, 0, 38000, 270)
    OP_4A(0x0008, 255)
    ChrSetChipByIndex(0x0008, 8)
    ChrSetSubChip(0x0008, 7)
    ChrClearFlags(0x000A, 0x0080)

    Jump('loc_306')

    def _loc_2BA(): pass

    label('loc_2BA')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0303, 4, 0x181C)),
            Expr.Return,
        ),
        'loc_2F2',
    )

    ChrSetFlags(0x000C, 0x0010)
    ChrSetPos(0x0008, -41180, 0, 38000, 270)
    OP_4A(0x0008, 255)
    ChrSetChipByIndex(0x0008, 8)
    ChrSetSubChip(0x0008, 7)
    ChrClearFlags(0x000A, 0x0080)
    ChrSetFlags(0x000F, 0x0080)

    Jump('loc_306')

    def _loc_2F2(): pass

    label('loc_2F2')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0301, 4, 0x180C)),
            Expr.Return,
        ),
        'loc_306',
    )

    ChrSetFlags(0x0008, 0x0080)
    ChrSetFlags(0x000F, 0x0080)

    Jump('loc_306')

    def _loc_306(): pass

    label('loc_306')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x021E, 0, 0x10F0)),
            Expr.Return,
        ),
        'loc_317',
    )

    ClearScenaFlags(ScenaFlag(0x021E, 0, 0x10F0))
    Event(0, func_0C_302F)

    Jump('loc_325')

    def _loc_317(): pass

    label('loc_317')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x021E, 1, 0x10F1)),
            Expr.Return,
        ),
        'loc_325',
    )

    ClearScenaFlags(ScenaFlag(0x021E, 1, 0x10F1))
    Event(1, 0x0003)

    def _loc_325(): pass

    label('loc_325')

    Return()

# id: 0x0001 offset: 0x326
@scena.Code('func_01_326')
def func_01_326():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0340, 0, 0x1A00)),
            Expr.Return,
        ),
        'loc_330',
    )

    Jump('loc_35C')

    def _loc_330(): pass

    label('loc_330')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0304, 2, 0x1822)),
            Expr.Return,
        ),
        'loc_341',
    )

    OP_6F(0x0002, 15)

    Jump('loc_35C')

    def _loc_341(): pass

    label('loc_341')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0303, 4, 0x181C)),
            Expr.Return,
        ),
        'loc_352',
    )

    OP_6F(0x0002, 15)

    Jump('loc_35C')

    def _loc_352(): pass

    label('loc_352')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0301, 4, 0x180C)),
            Expr.Return,
        ),
        'loc_35C',
    )

    Jump('loc_35C')

    def _loc_35C(): pass

    label('loc_35C')

    Return()

# id: 0x0002 offset: 0x35D
@scena.Code('func_02_35D')
def func_02_35D():
    ExecExpressionWithReg(
        0x000E,
        (
            Expr.Rand,
            (Expr.PushLong, 0xE),
            Expr.Mod,
            Expr.Nop,
            Expr.Return,
        ),
    )

    If(
        (
            (Expr.PushReg, 0xE),
            (Expr.PushLong, 0x0),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_382',
    )

    OP_99(0x00FE, 0x00, 0x07, 1650)

    Jump('loc_4C4')

    def _loc_382(): pass

    label('loc_382')

    If(
        (
            (Expr.PushReg, 0xE),
            (Expr.PushLong, 0x1),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_39B',
    )

    OP_99(0x00FE, 0x01, 0x07, 1600)

    Jump('loc_4C4')

    def _loc_39B(): pass

    label('loc_39B')

    If(
        (
            (Expr.PushReg, 0xE),
            (Expr.PushLong, 0x2),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_3B4',
    )

    OP_99(0x00FE, 0x02, 0x07, 1550)

    Jump('loc_4C4')

    def _loc_3B4(): pass

    label('loc_3B4')

    If(
        (
            (Expr.PushReg, 0xE),
            (Expr.PushLong, 0x3),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_3CD',
    )

    OP_99(0x00FE, 0x03, 0x07, 1500)

    Jump('loc_4C4')

    def _loc_3CD(): pass

    label('loc_3CD')

    If(
        (
            (Expr.PushReg, 0xE),
            (Expr.PushLong, 0x4),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_3E6',
    )

    OP_99(0x00FE, 0x04, 0x07, 1450)

    Jump('loc_4C4')

    def _loc_3E6(): pass

    label('loc_3E6')

    If(
        (
            (Expr.PushReg, 0xE),
            (Expr.PushLong, 0x5),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_3FF',
    )

    OP_99(0x00FE, 0x05, 0x07, 1400)

    Jump('loc_4C4')

    def _loc_3FF(): pass

    label('loc_3FF')

    If(
        (
            (Expr.PushReg, 0xE),
            (Expr.PushLong, 0x6),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_418',
    )

    OP_99(0x00FE, 0x06, 0x07, 1350)

    Jump('loc_4C4')

    def _loc_418(): pass

    label('loc_418')

    If(
        (
            (Expr.PushReg, 0xE),
            (Expr.PushLong, 0x7),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_431',
    )

    OP_99(0x00FE, 0x00, 0x07, 1655)

    Jump('loc_4C4')

    def _loc_431(): pass

    label('loc_431')

    If(
        (
            (Expr.PushReg, 0xE),
            (Expr.PushLong, 0x8),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_44A',
    )

    OP_99(0x00FE, 0x01, 0x07, 1605)

    Jump('loc_4C4')

    def _loc_44A(): pass

    label('loc_44A')

    If(
        (
            (Expr.PushReg, 0xE),
            (Expr.PushLong, 0x9),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_463',
    )

    OP_99(0x00FE, 0x02, 0x07, 1555)

    Jump('loc_4C4')

    def _loc_463(): pass

    label('loc_463')

    If(
        (
            (Expr.PushReg, 0xE),
            (Expr.PushLong, 0xA),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_47C',
    )

    OP_99(0x00FE, 0x03, 0x07, 1505)

    Jump('loc_4C4')

    def _loc_47C(): pass

    label('loc_47C')

    If(
        (
            (Expr.PushReg, 0xE),
            (Expr.PushLong, 0xB),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_495',
    )

    OP_99(0x00FE, 0x04, 0x07, 1455)

    Jump('loc_4C4')

    def _loc_495(): pass

    label('loc_495')

    If(
        (
            (Expr.PushReg, 0xE),
            (Expr.PushLong, 0xC),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_4AE',
    )

    OP_99(0x00FE, 0x05, 0x07, 1405)

    Jump('loc_4C4')

    def _loc_4AE(): pass

    label('loc_4AE')

    If(
        (
            (Expr.PushReg, 0xE),
            (Expr.PushLong, 0xD),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_4C4',
    )

    OP_99(0x00FE, 0x06, 0x07, 1355)

    def _loc_4C4(): pass

    label('loc_4C4')

    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_4D9',
    )

    OP_99(0x00FE, 0x00, 0x07, 1500)

    Jump('loc_4C4')

    def _loc_4D9(): pass

    label('loc_4D9')

    Return()

# id: 0x0003 offset: 0x4DA
@scena.Code('func_03_4DA')
def func_03_4DA():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_4FD',
    )

    OP_8D(0x00FE, -447, 33095, 4354, 30386, 4000)

    Jump('func_03_4DA')

    def _loc_4FD(): pass

    label('loc_4FD')

    Return()

# id: 0x0004 offset: 0x4FE
@scena.Code('func_04_4FE')
def func_04_4FE():
    TalkBegin(0x000B)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 0, 0x2000)),
            Expr.Return,
        ),
        'loc_87E',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0413, 3, 0x209B)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_71B',
    )

    OP_62(0x00FE, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    ChrTurnDirection(0x00FE, 0x0102, 0)
    Sleep(1000)

    ChrTalk(
        0x00FE,
        (
            '哟，艾丝蒂尔啊……\n',
            '这，这不是约修亚吗！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#1035F好久不见了，菲特先生。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '哟，才多久没见啊，\n',
            '就完全长成个男子汉了嘛。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '嗯，这我就放心了。\n',
            '和艾丝蒂尔在游击士的道路上都\n',
            '做得很漂亮嘛。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#1040F这都是托您的福。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '看来王国中\n',
            '好象发生了严重的事。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '回归军队的卡西乌斯\n',
            '也忙得不可开交吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x00FE, 0x0101, 400)

    ChrTalk(
        0x00FE,
        (
            '作为游击士的你们两个\n',
            '可要努力，不能输给他哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#1006F嗯！\n',
            '我们会尽全力完成工作的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#1040F有什么困难\n',
            '就联系协会吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x00FE, 0x0102, 400)

    ChrTalk(
        0x00FE,
        (
            '我会的。\n',
            '那么，两人都要小心。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0413, 3, 0x209B))

    Jump('loc_87B')

    def _loc_71B(): pass

    label('loc_71B')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 1, 0x1)),
            Expr.Return,
        ),
        'loc_761',
    )

    ChrTalk(
        0x00FE,
        (
            '有什么事我\n',
            '会联络协会的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '那么，两人都要小心。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ClearScenaFlags(ScenaFlag(0x0000, 1, 0x1))

    Jump('loc_87B')

    def _loc_761(): pass

    label('loc_761')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_823',
    )

    ChrTalk(
        0x00FE,
        (
            '这么说来，礼拜堂\n',
            '好像在举行婚礼……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '虽然是大喜的日子，\n',
            '却碰上事件实在是不走运。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我也是有女儿的父亲，\n',
            '理解父母的难处。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '唉，希望尤妮\n',
            '结婚的时候别发生什么事就好。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 0, 0x0))

    Jump('loc_87B')

    def _loc_823(): pass

    label('loc_823')

    ChrTalk(
        0x00FE,
        (
            '虽然是大喜的日子\n',
            '碰上这样的事件……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '唉，希望尤妮\n',
            '结婚的时候别发生什么事就好。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_87B(): pass

    label('loc_87B')

    Jump('loc_10C3')

    def _loc_87E(): pass

    label('loc_87E')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0340, 0, 0x1A00)),
            Expr.Return,
        ),
        'loc_948',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Return,
        ),
        'loc_8D4',
    )

    ChrTalk(
        0x00FE,
        (
            '怎么能让尤妮离开我。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '真让人感动……\n',
            '天下父母心都是相通的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_945')

    def _loc_8D4(): pass

    label('loc_8D4')

    ChrTalk(
        0x00FE,
        (
            '虽说可以出去了，\n',
            '还是不能让尤妮离开我。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '……亲子深情\n',
            '到任何地方都是一样的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '真是……太感人了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 0, 0x0))

    def _loc_945(): pass

    label('loc_945')

    Jump('loc_10C3')

    def _loc_948(): pass

    label('loc_948')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0304, 2, 0x1822)),
            Expr.Return,
        ),
        'loc_A36',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Return,
        ),
        'loc_9B9',
    )

    ChrTalk(
        0x00FE,
        (
            '虽说阿斯顿的部队来了，\n',
            '但雾没散之前都不能疏忽大意。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '总之不能让女儿尤妮\n',
            '离开我的视线。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_A33')

    def _loc_9B9(): pass

    label('loc_9B9')

    ChrTalk(
        0x00FE,
        (
            '看来阿斯顿的部队\n',
            '已经开始城市警备了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '可是，雾没散之前\n',
            '还是不能安心。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '总之不能让女儿尤妮\n',
            '离开我的视线。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 0, 0x0))

    def _loc_A33(): pass

    label('loc_A33')

    Jump('loc_10C3')

    def _loc_A36(): pass

    label('loc_A36')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0303, 4, 0x181C)),
            Expr.Return,
        ),
        'loc_B55',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Return,
        ),
        'loc_AAB',
    )

    ChrTalk(
        0x00FE,
        (
            '尤妮也一直\n',
            '不敢看我……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '虽说是为了保护女儿，\n',
            '发火也不像是平常的我……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '真让人沮丧……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_B52')

    def _loc_AAB(): pass

    label('loc_AAB')

    ChrTalk(
        0x00FE,
        (
            '今天早上，尤妮\n',
            '不听话想要跑出门。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我发现的时候\n',
            '就大声骂了她几句。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '虽说是为了女儿的安全，\n',
            '但如此失态真是太不像我了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '不知道会不会\n',
            '被尤妮讨厌……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 0, 0x0))

    def _loc_B52(): pass

    label('loc_B52')

    Jump('loc_10C3')

    def _loc_B55(): pass

    label('loc_B55')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0301, 4, 0x180C)),
            Expr.Return,
        ),
        'loc_EFB',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0312, 0, 0x1890)),
            Expr.Return,
        ),
        'loc_D12',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 1, 0x1)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_C7E',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Return,
        ),
        'loc_BC8',
    )

    ChrTalk(
        0x00FE,
        (
            '差不多到了互不侵犯条约的签字议式了吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '说得乐观点，\n',
            '这个国家前途光明啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_C7B')

    def _loc_BC8(): pass

    label('loc_BC8')

    ChrTalk(
        0x00FE,
        (
            '说起来，差不多是\n',
            '互不侵犯条约的签字议式了吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '卡西乌斯一定也为了警备什么的\n',
            '忙得不可开交吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '不过，因为这是对王国的将来\n',
            '举足轻重的条约啊。\n',
            '希望能平安签订下来啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 0, 0x0))

    def _loc_C7B(): pass

    label('loc_C7B')

    Jump('loc_D0F')

    def _loc_C7E(): pass

    label('loc_C7E')

    ChrTalk(
        0x00FE,
        (
            '洛连特支部由于人手不足，\n',
            '这阵子真是快忙翻了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '不但少了卡西乌斯，\n',
            '雪拉扎德也经常不在。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '这次两人一起回来了，\n',
            '就麻烦你们补这个空啦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    def _loc_D0F(): pass

    label('loc_D0F')

    Jump('loc_EF8')

    def _loc_D12(): pass

    label('loc_D12')

    OP_62(0x00FE, 0x00000000, 2000, 0x26, 0x26, 0x000000FA, 0x01)
    ChrTurnDirection(0x00FE, 0x0101, 0)
    Sleep(400)

    ChrTalk(
        0x00FE,
        (
            '哦，这不是艾丝蒂尔\n',
            '和雪拉扎德吗。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '好久不见啦。\n',
            '还好吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#1016F嗯，很好。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#020F事情很多，一直忙得很呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0206, 4, 0x1034)),
            Expr.Return,
        ),
        'loc_E09',
    )

    ChrTalk(
        0x00FE,
        (
            '是吗……\n',
            '两人都很有精神，这就太好了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '看来正游击士的任务\n',
            '都完成得很好嘛。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_E61')

    def _loc_E09(): pass

    label('loc_E09')

    ChrTalk(
        0x00FE,
        (
            '听爱娜说了，艾丝蒂尔\n',
            '也当上正游击士了嘛。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '哎呀哎呀，真是佩服。\n',
            '干得很不错嘛。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_E61(): pass

    label('loc_E61')

    ChrTalk(
        0x0101,
        (
            '#1008F嘿嘿……\n',
            '嗯，目前为止是还不错啦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '洛连特支部由于人手不足，\n',
            '这阵子看来真是快忙翻了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '期待艾丝蒂尔\n',
            '连卡西乌斯的份一起活跃啦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0312, 0, 0x1890))
    SetScenaFlags(ScenaFlag(0x0000, 1, 0x1))
    def _loc_EF8(): pass

    label('loc_EF8')

    Jump('loc_10C3')

    def _loc_EFB(): pass

    label('loc_EFB')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0200, 3, 0x1003)),
            Expr.Return,
        ),
        'loc_10C3',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0206, 4, 0x1034)),
            Expr.Return,
        ),
        'loc_F7D',
    )

    ChrTalk(
        0x00FE,
        (
            '政变是令人吃惊，\n',
            '但从结果来说，或许\n',
            '成为了王国整顿的契机。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '能够把光明的未来\n',
            '托付给孩子们就最好不过了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_10C3')

    def _loc_F7D(): pass

    label('loc_F7D')

    ChrTalk(
        0x00FE,
        (
            '艾丝蒂尔……\n',
            '几时回来的？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#000F刚刚才到飞船坪呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我听爱娜说了哦。\n',
            '你也成为正游击士了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '看来这趟旅行\n',
            '对你来说很有意义呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#008F嘿嘿，算是……吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '还听说卡西乌斯先生\n',
            '也回到王国军去了，是吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '政变是令人吃惊，\n',
            '但从结果来说，\n',
            '或许倒是个契机。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '能够把光明的未来\n',
            '托付给孩子们就最好不过了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0206, 4, 0x1034))

    def _loc_10C3(): pass

    label('loc_10C3')

    TalkEnd(0x000B)

    Return()

# id: 0x0005 offset: 0x10C7
@scena.Code('func_05_10C7')
def func_05_10C7():
    TalkBegin(0x000C)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0410, 5, 0x2085)),
            Expr.Return,
        ),
        'loc_1111',
    )

    ChrTalk(
        0x00FE,
        (
            '真是的～爸爸又\n',
            '开始自己胡乱担忧了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我才７岁呢……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_154F')

    def _loc_1111(): pass

    label('loc_1111')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 0, 0x2000)),
            Expr.Return,
        ),
        'loc_11E0',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 2, 0x2)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_1194',
    )

    ChrTalk(
        0x00FE,
        (
            '爸爸要出门，\n',
            '所以尤妮看家。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '不过，连灯也点不着，\n',
            '一个人的话真有点害怕啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '爸爸，早点回来……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 2, 0x2))

    Jump('loc_11DD')

    def _loc_1194(): pass

    label('loc_1194')

    ChrTalk(
        0x00FE,
        (
            '房间的灯都点不着，\n',
            '一个人的话真有点害怕……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '爸爸，早点回来……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_11DD(): pass

    label('loc_11DD')

    Jump('loc_154F')

    def _loc_11E0(): pass

    label('loc_11E0')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0340, 0, 0x1A00)),
            Expr.Return,
        ),
        'loc_122E',
    )

    ChrTalk(
        0x00FE,
        (
            '嘿嘿，今天\n',
            '一直和爸爸一起在哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '因为尤妮\n',
            '最喜欢爸爸了嘛。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_154F')

    def _loc_122E(): pass

    label('loc_122E')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0304, 2, 0x1822)),
            Expr.Return,
        ),
        'loc_1325',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 2, 0x2)),
            Expr.Return,
        ),
        'loc_127A',
    )

    ChrTalk(
        0x00FE,
        (
            '尤妮，要对爸爸道歉……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我说爸爸……\n',
            '『最坏』了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1322')

    def _loc_127A(): pass

    label('loc_127A')

    ChrTalk(
        0x00FE,
        (
            '听说士兵们\n',
            '在外面守着是真的？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '外面那么危险\n',
            '我一点儿也不知道……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '所以爸爸才不让\n',
            '尤妮出去吧……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '……尤妮，要对爸爸道歉才行。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '说爸爸最坏了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 2, 0x2))

    def _loc_1322(): pass

    label('loc_1322')

    Jump('loc_154F')

    def _loc_1325(): pass

    label('loc_1325')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0303, 4, 0x181C)),
            Expr.Return,
        ),
        'loc_137A',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 2, 0x2)),
            Expr.Return,
        ),
        'loc_1348',
    )

    ChrTalk(
        0x00FE,
        (
            '爸爸好坏……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1377')

    def _loc_1348(): pass

    label('loc_1348')

    ChrTalk(
        0x00FE,
        (
            '爸爸好坏……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '人家以后不理他了啦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 2, 0x2))

    def _loc_1377(): pass

    label('loc_1377')

    Jump('loc_154F')

    def _loc_137A(): pass

    label('loc_137A')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0301, 4, 0x180C)),
            Expr.Return,
        ),
        'loc_1449',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 2, 0x2)),
            Expr.Return,
        ),
        'loc_13BE',
    )

    ChrTalk(
        0x00FE,
        (
            '就说今天一步\n',
            '也不能出去。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '……爸爸真坏。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1446')

    def _loc_13BE(): pass

    label('loc_13BE')

    ChrTalk(
        0x00FE,
        (
            '啊，艾丝蒂尔姐姐！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '嗯嗯，听我说啦。\n',
            '爸爸好过分哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '竟然说尤妮\n',
            '不能出门哦？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我说这点雾不算什么啦，\n',
            '他都完全不听。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 2, 0x2))

    def _loc_1446(): pass

    label('loc_1446')

    Jump('loc_154F')

    def _loc_1449(): pass

    label('loc_1449')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0200, 3, 0x1003)),
            Expr.Return,
        ),
        'loc_154F',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 2, 0x2)),
            Expr.Return,
        ),
        'loc_14A2',
    )

    ChrTalk(
        0x00FE,
        (
            '对了对了，姐姐，\n',
            '见到鲁克了吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '鲁克真是的，\n',
            '总是说起姐姐哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_154F')

    def _loc_14A2(): pass

    label('loc_14A2')

    ChrTalk(
        0x00FE,
        (
            '啊，艾丝蒂尔姐姐！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#001F尤妮，还好吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '嗯，很好哦！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '对了对了，姐姐，\n',
            '见到鲁克了吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '鲁克真是的，\n',
            '总是说起姐姐哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#505F鲁克他？嗯…………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 2, 0x2))

    def _loc_154F(): pass

    label('loc_154F')

    TalkEnd(0x000C)

    Return()

# id: 0x0006 offset: 0x1553
@scena.Code('func_06_1553')
def func_06_1553():
    TalkBegin(0x0008)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0410, 6, 0x2086)),
            Expr.Return,
        ),
        'loc_166D',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 3, 0x3)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_160D',
    )

    ChrTalk(
        0x00FE,
        (
            '唔唔……真奇怪。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '婚礼应该结束了，\n',
            '女儿夫妇俩却还没回来。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '唔，在哪儿\n',
            '耽搁了呢……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '哈哈哈。\n',
            '算了，',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '他们俩感情越好，\n',
            '我就可以越快抱孙子啦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 3, 0x3))

    Jump('loc_166A')

    def _loc_160D(): pass

    label('loc_160D')

    ChrTalk(
        0x00FE,
        (
            '看来女儿夫妇俩\n',
            '是在哪儿耽搁了吧……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '也好。\n',
            '他们俩感情越好，\n',
            '我就可以越快抱孙子了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_166A(): pass

    label('loc_166A')

    Jump('loc_191E')

    def _loc_166D(): pass

    label('loc_166D')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0410, 5, 0x2085)),
            Expr.Return,
        ),
        'loc_1762',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 3, 0x3)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_170D',
    )

    ChrTalk(
        0x00FE,
        (
            '哎呀，有什么事呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '女儿夫妇俩去参加\n',
            '礼拜堂的婚礼了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '新郎新娘接受\n',
            '年轻夫妇的祝福……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '哈哈哈。\n',
            '哎呀，多么美丽的一幕哟。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 3, 0x3))

    Jump('loc_175F')

    def _loc_170D(): pass

    label('loc_170D')

    ChrTalk(
        0x00FE,
        (
            '女儿夫妇俩去参加\n',
            '礼拜堂的婚礼了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '可是这种时候举行婚礼\n',
            '真是有点可怜哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_175F(): pass

    label('loc_175F')

    Jump('loc_191E')

    def _loc_1762(): pass

    label('loc_1762')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 0, 0x2000)),
            Expr.Return,
        ),
        'loc_181B',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 3, 0x3)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_17D2',
    )

    If(
        (
            (Expr.Eval, "OP_29(0x0075, 0x00, 0x10)"),
            Expr.Return,
        ),
        'loc_178F',
    )

    ChrTalk(
        0x00FE,
        (
            '哦，是你们啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_178F(): pass

    label('loc_178F')

    ChrTalk(
        0x00FE,
        (
            '不知怎么的我家的导力器\n',
            '都不能用了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '这是故障吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 3, 0x3))

    Jump('loc_1818')

    def _loc_17D2(): pass

    label('loc_17D2')

    ChrTalk(
        0x00FE,
        (
            '我家的导力器\n',
            '不能动了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '唔，稍后让胡里奥那家伙\n',
            '去趟工房吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    def _loc_1818(): pass

    label('loc_1818')

    Jump('loc_191E')

    def _loc_181B(): pass

    label('loc_181B')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0200, 3, 0x1003)),
            Expr.Return,
        ),
        'loc_191E',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 3, 0x3)),
            Expr.Return,
        ),
        'loc_1879',
    )

    ChrTalk(
        0x00FE,
        (
            '他还得多多学习些东西。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '继我之后，背负\n',
            '洛连特林业重任的就只有他了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_191E')

    def _loc_1879(): pass

    label('loc_1879')

    ChrTalk(
        0x00FE,
        (
            '神秘森林里\n',
            '生长着塞尔贝的大树……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '传说以前\n',
            '就有喜欢恶作剧的精灵在那居住。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '让人看见幻象，\n',
            '在雾中迷失方向……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '嗯，就是类似\n',
            '古老传说那样的东西。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 3, 0x3))

    def _loc_191E(): pass

    label('loc_191E')

    TalkEnd(0x0008)

    Return()

# id: 0x0007 offset: 0x1922
@scena.Code('func_07_1922')
def func_07_1922():
    TalkBegin(0x000A)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0304, 2, 0x1822)),
            Expr.Return,
        ),
        'loc_19E8',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 4, 0x4)),
            Expr.Return,
        ),
        'loc_1973',
    )

    ChrTalk(
        0x00FE,
        (
            '这时候没工作真是帮大忙了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '这样我也能\n',
            '照顾岳父了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_19E5')

    def _loc_1973(): pass

    label('loc_1973')

    ChrTalk(
        0x00FE,
        (
            '现在刚好植树造林\n',
            '也告一段落了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '木材也没法出货，\n',
            '目前暂时休业的状态。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '嗯，因此就能\n',
            '照顾岳父了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 4, 0x4))

    def _loc_19E5(): pass

    label('loc_19E5')

    Jump('loc_1AA0')

    def _loc_19E8(): pass

    label('loc_19E8')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0303, 4, 0x181C)),
            Expr.Return,
        ),
        'loc_1AA0',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 4, 0x4)),
            Expr.Return,
        ),
        'loc_1A3A',
    )

    ChrTalk(
        0x00FE,
        (
            '岳父的睡着的样子\n',
            '看来非常幸福呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '到底做着怎样的梦呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1AA0')

    def _loc_1A3A(): pass

    label('loc_1A3A')

    ChrTalk(
        0x00FE,
        (
            '啊，今天也来了啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '岳父还是\n',
            '没有醒过来。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '只有一点欣慰的是\n',
            '他的睡脸\n',
            '看起来相当幸福。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 4, 0x4))

    def _loc_1AA0(): pass

    label('loc_1AA0')

    TalkEnd(0x000A)

    Return()

# id: 0x0008 offset: 0x1AA4
@scena.Code('func_08_1AA4')
def func_08_1AA4():
    TalkBegin(0x0009)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0340, 0, 0x1A00)),
            Expr.Return,
        ),
        'loc_1DAD',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x034B, 4, 0x1A5C)),
            Expr.Return,
        ),
        'loc_1BA9',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 5, 0x5)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_1B43',
    )

    ChrTalk(
        0x00FE,
        (
            '父亲真是的，一醒来\n',
            '就让老公去工作了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '一整晚都照看着他，\n',
            '还突然让人家工作……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '就算关系好了\n',
            '一提到工作还是那么严厉。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1BA6')

    def _loc_1B43(): pass

    label('loc_1B43')

    ChrTalk(
        0x00FE,
        (
            '此次一切\n',
            '都承蒙关照了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '父亲的情况我们\n',
            '也会多加注意的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '那么，你们也\n',
            '要多加小心哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1BA6(): pass

    label('loc_1BA6')

    Jump('loc_1DAA')

    def _loc_1BA9(): pass

    label('loc_1BA9')

    ChrTurnDirection(0x00FE, 0x0101, 0)

    ChrTalk(
        0x00FE,
        (
            '啊，是你们……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '太好了，父亲平安\n',
            '醒过来了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '真的……\n',
            '不知道该怎么感谢你们才好。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#1025F不用，别这么客气……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#020F那么，令尊的情况如何？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x00FE, 0x0103, 400)

    ChrTalk(
        0x00FE,
        (
            '嗯，非常精神哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '虽然还有点迷糊，\n',
            '但我想很快就会好的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#1011F是吗……看来没事呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#026F是啊，我想应该没事了……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#020F不过如果有什么变化\n',
            '请立即联系教区长吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '他应该会告知\n',
            '适当的应对方法的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '嗯，谢谢。\n',
            '我们会注意观察的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '……你们也是，\n',
            '要多加小心哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#1006F嗯，谢谢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#020F……那么，先告辞了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x034B, 4, 0x1A5C))
    SetScenaFlags(ScenaFlag(0x0000, 5, 0x5))
    def _loc_1DAA(): pass

    label('loc_1DAA')

    Jump('loc_20D4')

    def _loc_1DAD(): pass

    label('loc_1DAD')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0304, 2, 0x1822)),
            Expr.Return,
        ),
        'loc_1EB7',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 5, 0x5)),
            Expr.Return,
        ),
        'loc_1E27',
    )

    ChrTalk(
        0x00FE,
        (
            '这么担心父亲\n',
            '真是令人感激……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '这样下去说不定\n',
            '他才让我更伤脑筋呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '今天可得\n',
            '换我来照顾了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1EB4')

    def _loc_1E27(): pass

    label('loc_1E27')

    ChrTalk(
        0x00FE,
        (
            '老公也是不眠不休地\n',
            '照料着父亲呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我说换我来，\n',
            '他都不肯离开……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '这样下去\n',
            '他才让我更伤脑筋呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '今天可得\n',
            '换我来照顾了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 5, 0x5))

    def _loc_1EB4(): pass

    label('loc_1EB4')

    Jump('loc_20D4')

    def _loc_1EB7(): pass

    label('loc_1EB7')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0303, 4, 0x181C)),
            Expr.Return,
        ),
        'loc_1F9A',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 5, 0x5)),
            Expr.Return,
        ),
        'loc_1F10',
    )

    ChrTalk(
        0x00FE,
        (
            '雾看起来好像\n',
            '比昨天更浓了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '不管怎样，希望\n',
            '别再发生任何事了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1F97')

    def _loc_1F10(): pass

    label('loc_1F10')

    ChrTalk(
        0x00FE,
        (
            '雾看起来好像\n',
            '比昨天更浓了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '父亲仍旧\n',
            '在安睡着……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '不管怎样，希望\n',
            '别再发生任何事了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '女神啊……\n',
            '求求你救救他吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 5, 0x5))

    def _loc_1F97(): pass

    label('loc_1F97')

    Jump('loc_20D4')

    def _loc_1F9A(): pass

    label('loc_1F9A')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0301, 4, 0x180C)),
            Expr.Return,
        ),
        'loc_2072',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 5, 0x5)),
            Expr.Return,
        ),
        'loc_1FEF',
    )

    ChrTalk(
        0x00FE,
        (
            '父亲最近也\n',
            '接受了老公。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '……事情太顺利\n',
            '甚至觉得有点可怕。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_206F')

    def _loc_1FEF(): pass

    label('loc_1FEF')

    ChrTalk(
        0x00FE,
        (
            '老公胡里奥，以前\n',
            '只知道拼命工作的……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '最近却感觉好像\n',
            '沉着稳重多了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '和父亲也相处得很好，\n',
            '是抓住了工作要领吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 5, 0x5))

    def _loc_206F(): pass

    label('loc_206F')

    Jump('loc_20D4')

    def _loc_2072(): pass

    label('loc_2072')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0200, 3, 0x1003)),
            Expr.Return,
        ),
        'loc_20D4',
    )

    ChrTalk(
        0x00FE,
        (
            '老公的工作非常顺利。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '和父亲也相处得很好，\n',
            '真是太好了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '……我现在非常幸福。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_20D4(): pass

    label('loc_20D4')

    TalkEnd(0x0009)

    Return()

# id: 0x0009 offset: 0x20D8
@scena.Code('func_09_20D8')
def func_09_20D8():
    TalkBegin(0x000F)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0340, 0, 0x1A00)),
            Expr.Return,
        ),
        'loc_227E',
    )

    If(
        (
            (Expr.Eval, "OP_29(0x0077, 0x00, 0x08)"),
            Expr.Return,
        ),
        'loc_21DC',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 3, 0xB)),
            Expr.Return,
        ),
        'loc_213A',
    )

    ChrTalk(
        0x000F,
        (
            '那么，委任书的事\n',
            '就拜托你们了！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000F,
        (
            '如果找到了，\n',
            '就马上回来。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_21D9')

    def _loc_213A(): pass

    label('loc_213A')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 6, 0x6)),
            Expr.Return,
        ),
        'loc_2192',
    )

    ChrTalk(
        0x000F,
        (
            '委任书的事……\n',
            '就拜托你们了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000F,
        (
            '因为这件事，我担心得\n',
            '都没心思工作了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_21D9')

    def _loc_2192(): pass

    label('loc_2192')

    ChrTalk(
        0x000F,
        (
            '啊，游击士。\n',
            '调查有进展吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000F,
        (
            '委任书的事……\n',
            '就拜托你们了！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 6, 0x6))

    def _loc_21D9(): pass

    label('loc_21D9')

    Jump('loc_227B')

    def _loc_21DC(): pass

    label('loc_21DC')

    If(
        (
            (Expr.Eval, "OP_29(0x0077, 0x00, 0x02)"),
            Expr.Return,
        ),
        'loc_21FF',
    )

    If(
        (
            (Expr.Eval, "OP_29(0x0077, 0x01, 0x8000)"),
            Expr.Return,
        ),
        'loc_21F8',
    )

    Call(1, 0x0001)

    Jump('loc_21FC')

    def _loc_21F8(): pass

    label('loc_21F8')

    Call(1, 0x0000)

    def _loc_21FC(): pass

    label('loc_21FC')

    Jump('loc_227B')

    def _loc_21FF(): pass

    label('loc_21FF')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 6, 0x6)),
            Expr.Return,
        ),
        'loc_2223',
    )

    ChrTalk(
        0x000F,
        (
            '唔～～……真伤脑筋。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_227B')

    def _loc_2223(): pass

    label('loc_2223')

    ChrTalk(
        0x000F,
        (
            '唔～～……真伤脑筋。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000F,
        (
            '好不容易到了要重新开工的时候，\n',
            '那东西却偏偏不见了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 6, 0x6))

    def _loc_227B(): pass

    label('loc_227B')

    Jump('loc_253A')

    def _loc_227E(): pass

    label('loc_227E')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0304, 2, 0x1822)),
            Expr.Return,
        ),
        'loc_23C1',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 6, 0x6)),
            Expr.Return,
        ),
        'loc_22E5',
    )

    ChrTalk(
        0x000F,
        (
            '山道出现了雾样的妖怪\n',
            '真是给吓了一大跳。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000F,
        (
            '游击士小哥用剑一砍，\n',
            '就烟消云散了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_23BE')

    def _loc_22E5(): pass

    label('loc_22E5')

    ChrTalk(
        0x000F,
        (
            '真伤脑筋……\n',
            '雾居然到山上来了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000F,
        (
            '工作没法继续，\n',
            '只能盲目等待时，\n',
            '协会发来了联络。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000F,
        (
            '说派了游击士来，\n',
            '所以就被护送回了城。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000F,
        (
            '从山道回来时，好几次\n',
            '被雾妖袭击。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000F,
        (
            '如果游击士没来，\n',
            '当真是危在旦夕啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 6, 0x6))

    def _loc_23BE(): pass

    label('loc_23BE')

    Jump('loc_253A')

    def _loc_23C1(): pass

    label('loc_23C1')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0200, 3, 0x1003)),
            Expr.Return,
        ),
        'loc_253A',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0206, 2, 0x1032)),
            Expr.Return,
        ),
        'loc_2411',
    )

    ChrTalk(
        0x000F,
        (
            '今天是陪伴家人的日子。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000F,
        (
            '最近由于工作\n',
            '一直窝在矿山里。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_253A')

    def _loc_2411(): pass

    label('loc_2411')

    ChrTalk(
        0x000F,
        (
            '……啊？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000F,
        (
            '这不是以前承蒙照顾的\n',
            '游击士小姑娘吗。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#501F啊，玛鲁加矿山的工头……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000F,
        (
            '多亏了你们，\n',
            '新矿脉的开采很顺利哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000F,
        (
            '在那之后，最后用炸药把\n',
            '魔兽出现的洞穴堵上了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#506F真，真是…啊哈哈…',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000F,
        (
            '嗯，没有其它办法了嘛。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000F,
        (
            '但是，多亏这个办法，\n',
            '现在的玛鲁加矿山景气多了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0206, 2, 0x1032))

    def _loc_253A(): pass

    label('loc_253A')

    TalkEnd(0x000F)

    Return()

# id: 0x000A offset: 0x253E
@scena.Code('func_0A_253E')
def func_0A_253E():
    TalkBegin(0x000D)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0410, 5, 0x2085)),
            Expr.Return,
        ),
        'loc_2653',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 7, 0x7)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_25FE',
    )

    ChrTalk(
        0x00FE,
        (
            '就在刚才\n',
            '老公突然回来了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '好像出了些麻烦事，\n',
            '但矿山的工作还是在继续。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '这种时候，\n',
            '早点回来多好……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '唉，他那人性格就是这样，\n',
            '无论怎么劝阻也是没用的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 7, 0x7))

    Jump('loc_2650')

    def _loc_25FE(): pass

    label('loc_25FE')

    ChrTalk(
        0x00FE,
        (
            '刚才老公\n',
            '从矿山回来了哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '好像出了些麻烦事，\n',
            '但今天好像还要继续工作呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_2650(): pass

    label('loc_2650')

    Jump('loc_2C2A')

    def _loc_2653(): pass

    label('loc_2653')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 0, 0x2000)),
            Expr.Return,
        ),
        'loc_2722',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 7, 0x7)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_26D5',
    )

    ChrTalk(
        0x00FE,
        (
            '导力器都停止了，\n',
            '真的很让人担心啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '正好矿山\n',
            '才刚刚开始工程。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '别发生什么\n',
            '事故或麻烦就好……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 7, 0x7))

    Jump('loc_271F')

    def _loc_26D5(): pass

    label('loc_26D5')

    ChrTalk(
        0x00FE,
        (
            '导力器都停止了，\n',
            '真的很让人担心啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '正好矿山\n',
            '才刚刚开始工程。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_271F(): pass

    label('loc_271F')

    Jump('loc_2C2A')

    def _loc_2722(): pass

    label('loc_2722')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0340, 0, 0x1A00)),
            Expr.Return,
        ),
        'loc_2932',
    )

    If(
        (
            (Expr.Eval, "OP_29(0x0077, 0x00, 0x10)"),
            Expr.Return,
        ),
        'loc_284C',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 7, 0x7)),
            Expr.Return,
        ),
        'loc_2789',
    )

    ChrTalk(
        0x00FE,
        (
            '他那么努力\n',
            '也是为了我们家人嘛。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我也要尽一切力量，\n',
            '支撑老公才行。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2849')

    def _loc_2789(): pass

    label('loc_2789')

    ChrTalk(
        0x00FE,
        (
            '天刚晴\n',
            '马上就重新开工……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '玛鲁加矿山\n',
            '现在好像非常忙碌呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '都起了那么大的雾，\n',
            '稍微休息下就好了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '但是，他那么努力\n',
            '也是为了我们家人嘛。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '想到这个，\n',
            '也不能有怨言了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 7, 0x7))

    def _loc_2849(): pass

    label('loc_2849')

    Jump('loc_292F')

    def _loc_284C(): pass

    label('loc_284C')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 1, 0x9)),
            Expr.Return,
        ),
        'loc_28A2',
    )

    ChrTalk(
        0x00FE,
        (
            '老公好像\n',
            '给你们添麻烦了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '不管怎样，能够平安\n',
            '看他出门真是太好了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_292F')

    def _loc_28A2(): pass

    label('loc_28A2')

    ChrTalk(
        0x00FE,
        (
            '我家老公，今天应该\n',
            '开始矿山的工作了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '但现在还没出去呢，\n',
            '好像丢了什么重要的东西。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '真是的，其他矿工们的\n',
            '监督工作不要紧吗……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_292F(): pass

    label('loc_292F')

    Jump('loc_2C2A')

    def _loc_2932(): pass

    label('loc_2932')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0304, 2, 0x1822)),
            Expr.Return,
        ),
        'loc_2A1A',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 7, 0x7)),
            Expr.Return,
        ),
        'loc_2991',
    )

    ChrTalk(
        0x00FE,
        (
            '不管怎样，老公平安\n',
            '回来就比什么都重要了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '这些还都\n',
            '多亏了游击士们。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2A17')

    def _loc_2991(): pass

    label('loc_2991')

    ChrTalk(
        0x00FE,
        (
            '啊啊，太好了……\n',
            '老公平安从矿山回来了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '好像是游击士们\n',
            '一直护卫到城里来的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '雾居然都到了矿山……\n',
            '到底是怎么回事呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 7, 0x7))

    def _loc_2A17(): pass

    label('loc_2A17')

    Jump('loc_2C2A')

    def _loc_2A1A(): pass

    label('loc_2A1A')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0303, 4, 0x181C)),
            Expr.Return,
        ),
        'loc_2AD8',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 7, 0x7)),
            Expr.Return,
        ),
        'loc_2A64',
    )

    ChrTalk(
        0x00FE,
        (
            '老公平安\n',
            '到达矿山了吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '别在路上迷路就好了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2AD5')

    def _loc_2A64(): pass

    label('loc_2A64')

    ChrTalk(
        0x00FE,
        (
            '不得了了……\n',
            '今天早上雾不是也很大吗。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '真担心老公……\n',
            '平安到达矿山了吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '别在路上迷路就好了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 7, 0x7))

    def _loc_2AD5(): pass

    label('loc_2AD5')

    Jump('loc_2C2A')

    def _loc_2AD8(): pass

    label('loc_2AD8')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0301, 4, 0x180C)),
            Expr.Return,
        ),
        'loc_2BF4',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 7, 0x7)),
            Expr.Return,
        ),
        'loc_2B5E',
    )

    ChrTalk(
        0x00FE,
        (
            '也许因为很少见面，\n',
            '我家女儿和爸爸很亲。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '因此\n',
            '我们夫妇也很圆满。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '和他在一起１５年，\n',
            '都还没到疲劳期呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2BF1')

    def _loc_2B5E(): pass

    label('loc_2B5E')

    ChrTalk(
        0x00FE,
        (
            '老公去矿山\n',
            '已经４天了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '差不多是女儿开始\n',
            '想爸爸的时候了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '也许因为很少相见，\n',
            '真是个亲爸爸的孩子。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '因此\n',
            '我们夫妇也很圆满。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 7, 0x7))

    def _loc_2BF1(): pass

    label('loc_2BF1')

    Jump('loc_2C2A')

    def _loc_2BF4(): pass

    label('loc_2BF4')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0200, 3, 0x1003)),
            Expr.Return,
        ),
        'loc_2C2A',
    )

    ChrTalk(
        0x00FE,
        (
            '今天大家要一起出门，\n',
            '所以正在准备便当呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_2C2A(): pass

    label('loc_2C2A')

    TalkEnd(0x000D)

    Return()

# id: 0x000B offset: 0x2C2E
@scena.Code('func_0B_2C2E')
def func_0B_2C2E():
    TalkBegin(0x000E)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0410, 5, 0x2085)),
            Expr.Return,
        ),
        'loc_2C70',
    )

    ChrTalk(
        0x00FE,
        (
            '刚才爸爸回来了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '但是，马上又\n',
            '去工作了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_302B')

    def _loc_2C70(): pass

    label('loc_2C70')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 0, 0x2000)),
            Expr.Return,
        ),
        'loc_2CBC',
    )

    ChrTalk(
        0x00FE,
        (
            '妈妈也真是的，\n',
            '到底在想什么嘛～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '是不是\n',
            '有什么烦心事呢～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_302B')

    def _loc_2CBC(): pass

    label('loc_2CBC')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0340, 0, 0x1A00)),
            Expr.Return,
        ),
        'loc_2D5E',
    )

    If(
        (
            (Expr.Eval, "OP_29(0x0077, 0x00, 0x10)"),
            Expr.Return,
        ),
        'loc_2D24',
    )

    ChrTalk(
        0x00FE,
        (
            '啊……爸爸\n',
            '又去工作了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '这次的工作\n',
            '要去几天呢～？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '希望他早点回来……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2D5B')

    def _loc_2D24(): pass

    label('loc_2D24')

    ChrTalk(
        0x00FE,
        (
            '总觉得爸爸\n',
            '一脸烦恼的样子～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '怎～么回事呢……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_2D5B(): pass

    label('loc_2D5B')

    Jump('loc_302B')

    def _loc_2D5E(): pass

    label('loc_2D5E')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0304, 2, 0x1822)),
            Expr.Return,
        ),
        'loc_2E38',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 0, 0x8)),
            Expr.Return,
        ),
        'loc_2DBB',
    )

    ChrTalk(
        0x00FE,
        (
            '红头发的哥哥他们\n',
            '把爸爸带回来了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '嘿嘿……爸爸\n',
            '回来我真好高兴喔⊙',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2E35')

    def _loc_2DBB(): pass

    label('loc_2DBB')

    ChrTalk(
        0x00FE,
        (
            '红头发哥哥他们\n',
            '把爸爸带回来了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '听说矿山也起了雾，\n',
            '所以回来避难的～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '嘿嘿……不过，爸爸\n',
            '回来我好高兴喔⊙',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0001, 0, 0x8))

    def _loc_2E35(): pass

    label('loc_2E35')

    Jump('loc_302B')

    def _loc_2E38(): pass

    label('loc_2E38')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0303, 4, 0x181C)),
            Expr.Return,
        ),
        'loc_2EEF',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 0, 0x8)),
            Expr.Return,
        ),
        'loc_2E93',
    )

    ChrTalk(
        0x00FE,
        (
            '爸爸总是\n',
            '一早就出去工作。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '阿妮娅也起得很早，\n',
            '可总是见不到爸爸。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2EEC')

    def _loc_2E93(): pass

    label('loc_2E93')

    ChrTalk(
        0x00FE,
        (
            '爸爸总是\n',
            '一早就出去工作。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '阿妮娅也起得很早，\n',
            '可总是见不到爸爸。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '呜……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0001, 0, 0x8))

    def _loc_2EEC(): pass

    label('loc_2EEC')

    Jump('loc_302B')

    def _loc_2EEF(): pass

    label('loc_2EEF')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0301, 4, 0x180C)),
            Expr.Return,
        ),
        'loc_2FE0',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 0, 0x8)),
            Expr.Return,
        ),
        'loc_2F4A',
    )

    ChrTalk(
        0x00FE,
        (
            '阿妮娅已经\n',
            '好～久没见到爸爸了啦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '好想爸爸～\n',
            '然后再一起去郊游。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2FDD')

    def _loc_2F4A(): pass

    label('loc_2F4A')

    ChrTalk(
        0x00FE,
        (
            '爸爸的工作\n',
            '现在非常忙哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '阿妮娅已经\n',
            '好～久没见到爸爸了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '呜～呜，前阵子的\n',
            '郊游好开心哦～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '好想再和爸爸一起\n',
            '去帕赛尔农场哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0001, 0, 0x8))

    def _loc_2FDD(): pass

    label('loc_2FDD')

    Jump('loc_302B')

    def _loc_2FE0(): pass

    label('loc_2FE0')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0200, 3, 0x1003)),
            Expr.Return,
        ),
        'loc_302B',
    )

    ChrTalk(
        0x00FE,
        (
            '嘿嘿，今天\n',
            '爸爸说他放假。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '所以就带我去\n',
            '帕赛尔农场郊游了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_302B(): pass

    label('loc_302B')

    TalkEnd(0x000E)

    Return()

# id: 0x000C offset: 0x302F
@scena.Code('func_0C_302F')
def func_0C_302F():
    EventBegin(0x00)
    OP_DB()
    ChrSetFlags(0x0000, 0x0080)
    ChrSetFlags(0x0001, 0x0080)
    ChrSetFlags(0x0002, 0x0080)
    ChrSetFlags(0x0003, 0x0080)
    ChrSetPos(0x0008, -42510, 0, 37680, 238)
    ChrSetPos(0x0009, -43770, 0, 36860, 59)
    ChrSetPos(0x000A, -43000, 0, 36530, 10)
    ChrClearFlags(0x0008, 0x0080)
    ChrClearFlags(0x0009, 0x0080)
    ChrClearFlags(0x000A, 0x0080)
    ChrSetChipByIndex(0x0008, 0)
    ChrSetSubChip(0x0008, 0)
    CreateThread(0x000A, 0x00, 0x00, func_02_35D)
    OP_6F(0x0002, 0)
    CameraMove(-39410, 0, 35550, 0)
    OP_67(0, 6150, -10000, 0)
    CameraSetDistance(2750, 0)
    OP_6C(45000, 0)
    OP_6E(280, 0)
    FadeIn(1000, 0)

    @scena.Lambda('lambda_30EC')
    def lambda_30EC():
        CameraMove(-43060, 0, 37080, 3000)

        ExitThread()

    DispatchAsync(0x0000, 0x0001, lambda_30EC)

    Sleep(1500)

    OP_62(0x0009, 0x00000000, 2000, 0x26, 0x27, 0x000000FA, 0x02)
    Sleep(100)

    OP_62(0x000A, 0x00000000, 2000, 0x26, 0x27, 0x000000FA, 0x02)
    Sleep(1000)

    ChrJumpToRelative(0x0008, 0, 0, 0, 200, 4000)
    Sleep(500)

    ChrSetDirection(0x0008, 180, 400)
    ChrSetDirection(0x0008, 90, 400)
    ChrSetDirection(0x0008, 0, 400)
    ChrSetDirection(0x0008, 270, 400)
    ChrSetDirection(0x0008, 238, 400)
    Sleep(1000)

    FadeOut(1000, 0, -1)
    OP_0D()
    OP_DC()
    SetScenaFlags(ScenaFlag(0x021E, 0, 0x10F0))
    NewScene('ED6_DT21/T0410._SN', 110, 0, 0)
    IdleLoop()

    Return()

def main():
    scena.run(globals())

if __name__ == '__main__':
    Try(main)
