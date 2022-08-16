import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED62.Parser.scena_writer_helper import *
try:
    import C5510_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('C5510   ._SN')

# id: 0xFFFF offset: 0x0
@scena.Header('Header')
def Header():
    header = ScenaHeader()
    header.mapName        = 'Other'
    header.mapModel       = 'C5510.x'
    header.mapIndex       = 1
    header.bgm            = 34
    header.flags          = 0x0000
    header.entryFunction  = 0x0005
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
        ('ED6_DT29/CH12240._CH', 'ED6_DT29/CH12240P._CP'),
        ('ED6_DT29/CH12241._CH', 'ED6_DT29/CH12241P._CP'),
        ('ED6_DT29/CH12370._CH', 'ED6_DT29/CH12370P._CP'),
        ('ED6_DT29/CH12371._CH', 'ED6_DT29/CH12371P._CP'),
        ('ED6_DT29/CH12210._CH', 'ED6_DT29/CH12210P._CP'),
        ('ED6_DT29/CH12211._CH', 'ED6_DT29/CH12211P._CP'),
        ('ED6_DT29/CH12270._CH', 'ED6_DT29/CH12270P._CP'),
        ('ED6_DT29/CH12271._CH', 'ED6_DT29/CH12271P._CP'),
    ]

# id: 0x10001 offset: 0xEA
@scena.NpcData('NpcData')
def NpcData():
    return (
        ScenaNpcData(
            name                = '',
            x                   = 44500,
            z                   = 1000,
            y                   = -10740,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 6,
            chipIndex           = 6,
            npcIndex            = 0x01C5,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
    )

# id: 0x10002 offset: 0x10A
@scena.MonsterData('MonsterData')
def MonsterData():
    return (
        ScenaMonsterData(
            name        = '',
            x           = 2820,
            z           = 0,
            y           = 42410,
            word_0C     = 0x00B4,
            word_0E     = 0x0000,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x038D,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            name        = '',
            x           = 1060,
            z           = 0,
            y           = -82420,
            word_0C     = 0x00B4,
            word_0E     = 0x0000,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x038D,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            name        = '',
            x           = 8210,
            z           = 0,
            y           = -23060,
            word_0C     = 0x00B4,
            word_0E     = 0x0000,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x038D,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            name        = '',
            x           = -4160,
            z           = 0,
            y           = -33900,
            word_0C     = 0x00B4,
            word_0E     = 0x0000,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x038D,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            name        = '',
            x           = 2090,
            z           = 0,
            y           = -9120,
            word_0C     = 0x00B4,
            word_0E     = 0x0000,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x038D,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            name        = '',
            x           = -7920,
            z           = 0,
            y           = -37050,
            word_0C     = 0x00B4,
            word_0E     = 0x0000,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x038D,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
    )

# id: 0x10003 offset: 0x1B2
@scena.EventData('EventData')
def EventData():
    return (
    )

# id: 0x10004 offset: 0x1B2
@scena.ActorData('ActorData')
def ActorData():
    return (
        ScenaActorData(
            triggerX            = -40430,
            triggerZ            = 0,
            triggerY            = -25410,
            triggerRange        = 1000,
            actorX              = -40520,
            actorZ              = 0,
            actorY              = -24710,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0003,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = 44500,
            triggerZ            = 0,
            triggerY            = -11400,
            triggerRange        = 1000,
            actorX              = 44500,
            actorZ              = 0,
            actorY              = -10740,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0004,
            word_22             = 0x0000,
        ),
    )

# id: 0x0000 offset: 0x1FA
@scena.Code('Init')
def Init():
    Return()

# id: 0x0001 offset: 0x1FB
@scena.Code('func_01_1FB')
def func_01_1FB():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0228, 3, 0x1143)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_20D',
    )

    OP_6F(0x0007, 0)

    Jump('loc_214')

    def _loc_20D(): pass

    label('loc_20D')

    OP_6F(0x0007, 60)

    def _loc_214(): pass

    label('loc_214')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0228, 4, 0x1144)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_226',
    )

    OP_6F(0x0008, 0)

    Jump('loc_22D')

    def _loc_226(): pass

    label('loc_226')

    OP_6F(0x0008, 60)

    def _loc_22D(): pass

    label('loc_22D')

    If(
        (
            (Expr.PushValueByIndex, 0x0),
            (Expr.PushLong, 0x68),
            Expr.Equ,
            (Expr.PushValueByIndex, 0x0),
            (Expr.PushLong, 0x69),
            Expr.Equ,
            Expr.Or,
            (Expr.PushValueByIndex, 0x0),
            (Expr.PushLong, 0x6B),
            Expr.Equ,
            Expr.Or,
            (Expr.PushValueByIndex, 0x0),
            (Expr.PushLong, 0x6D),
            Expr.Equ,
            Expr.Or,
            Expr.Return,
        ),
        'loc_285',
    )

    OP_C4(0x00, 0x00000001)
    OP_78(0x00, 0x00, 0x00)
    OP_79(0x04, 0x0002)
    OP_79(0x05, 0x0002)
    OP_79(0x06, 0x0002)
    OP_79(0x07, 0x0002)
    OP_79(0x08, 0x0002)
    OP_79(0x09, 0x0002)
    OP_79(0x0A, 0x0002)
    OP_79(0x0B, 0x0002)
    OP_79(0x0C, 0x0002)

    Jump('loc_2AD')

    def _loc_285(): pass

    label('loc_285')

    OP_78(0xDC, 0xE6, 0xFF)
    OP_7A(0x04, 0x0002)
    OP_7A(0x05, 0x0002)
    OP_7A(0x06, 0x0002)
    OP_7A(0x07, 0x0002)
    OP_7A(0x08, 0x0002)
    OP_7A(0x09, 0x0002)
    OP_7A(0x0A, 0x0002)
    OP_7A(0x0B, 0x0002)
    OP_7A(0x0C, 0x0002)

    def _loc_2AD(): pass

    label('loc_2AD')

    Return()

# id: 0x0002 offset: 0x2AE
@scena.Code('func_02_2AE')
def func_02_2AE():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_2C3',
    )

    OP_99(0x00FE, 0x00, 0x07, 1500)

    Jump('func_02_2AE')

    def _loc_2C3(): pass

    label('loc_2C3')

    Return()

# id: 0x0003 offset: 0x2C4
@scena.Code('func_03_2C4')
def func_03_2C4():
    UnlockAchievement(0x02, 0x0199, 0x00)
    MapSetFlags(0x08000000)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0228, 3, 0x1143)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_3A1',
    )

    PlaySE(43, 0x00, 0x64)
    OP_70(0x0007, 60)
    Sleep(500)

    If(
        (
            (Expr.Eval, "AddItem(ItemTable['EP填充剂Ⅰ'], 1)"),
            Expr.Return,
        ),
        'loc_338',
    )

    FadeOut(300, 0, 100)
    PlaySE(17, 0x00, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    TalkSetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '得到了',
            (TxtCtl.Item, ItemTable['EP填充剂Ⅰ']),
            (TxtCtl.SetColor, 0x0),
            '。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)
    SetScenaFlags(ScenaFlag(0x0228, 3, 0x1143))

    Jump('loc_39E')

    def _loc_338(): pass

    label('loc_338')

    FadeOut(300, 0, 100)
    TalkSetChrName('')

    Talk(
        (
            '宝箱里装有',
            (TxtCtl.Item, ItemTable['EP填充剂Ⅰ']),
            (TxtCtl.SetColor, 0x0),
            '。   \n',
            '所持物品已经满了，',
            (TxtCtl.Item, ItemTable['EP填充剂Ⅰ']),
            (TxtCtl.SetColor, 0x0),
            '只能放弃了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    PlaySE(44, 0x00, 0x64)
    OP_6F(0x0007, 60)
    OP_70(0x0007, 0)

    def _loc_39E(): pass

    label('loc_39E')

    Jump('loc_3D2')

    def _loc_3A1(): pass

    label('loc_3A1')

    FadeOut(300, 0, 100)
    TalkSetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '宝箱中什么都没有。',
            (TxtCtl.SetColor, 0x0),
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    def _loc_3D2(): pass

    label('loc_3D2')

    Sleep(30)

    TalkEnd(0x00FF)
    MapClearFlags(0x08000000)

    Return()

# id: 0x0004 offset: 0x3E0
@scena.Code('func_04_3E0')
def func_04_3E0():
    UnlockAchievement(0x02, 0x019A, 0x00)
    MapSetFlags(0x08000000)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0228, 4, 0x1144)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_4BD',
    )

    PlaySE(43, 0x00, 0x64)
    OP_70(0x0008, 60)
    Sleep(500)

    If(
        (
            (Expr.Eval, "AddItem(ItemTable['夜视眼镜'], 1)"),
            Expr.Return,
        ),
        'loc_454',
    )

    FadeOut(300, 0, 100)
    PlaySE(17, 0x00, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    TalkSetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '得到了',
            (TxtCtl.Item, ItemTable['夜视眼镜']),
            (TxtCtl.SetColor, 0x0),
            '。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)
    SetScenaFlags(ScenaFlag(0x0228, 4, 0x1144))

    Jump('loc_4BA')

    def _loc_454(): pass

    label('loc_454')

    FadeOut(300, 0, 100)
    TalkSetChrName('')

    Talk(
        (
            '宝箱里装有',
            (TxtCtl.Item, ItemTable['夜视眼镜']),
            (TxtCtl.SetColor, 0x0),
            '。   \n',
            '所持物品已经满了，',
            (TxtCtl.Item, ItemTable['夜视眼镜']),
            (TxtCtl.SetColor, 0x0),
            '只能放弃了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    PlaySE(44, 0x00, 0x64)
    OP_6F(0x0008, 60)
    OP_70(0x0008, 0)

    def _loc_4BA(): pass

    label('loc_4BA')

    Jump('loc_4EE')

    def _loc_4BD(): pass

    label('loc_4BD')

    FadeOut(300, 0, 100)
    TalkSetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '宝箱中什么都没有。',
            (TxtCtl.SetColor, 0x0),
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    def _loc_4EE(): pass

    label('loc_4EE')

    Sleep(30)

    TalkEnd(0x00FF)
    MapClearFlags(0x08000000)

    Return()

# id: 0x0005 offset: 0x4FC
@scena.Code('func_05_4FC')
def func_05_4FC():
    If(
        (
            (Expr.PushValueByIndex, 0x13),
            (Expr.PushLong, 0x416),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_509',
    )

    Return()

    def _loc_509(): pass

    label('loc_509')

    MapSetFlags(0x00000080)
    OP_C0(0x01, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000)
    Sleep(30)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x020C, 7, 0x1067)),
            Expr.Return,
        ),
        'loc_59F',
    )

    TalkBegin(0x00FF)
    PlaySE(157, 0x00, 0x64)
    FadeOut(300, 0, 100)
    TalkSetChrName('')
    SetMessageWindowPos(-1, -1, -1, -1)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '认证组件已经启动了……\n',
            '但好像没什么特别的反应。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    TalkEnd(0x00FF)

    Jump('loc_895')

    def _loc_59F(): pass

    label('loc_59F')

    TalkBegin(0x00FF)
    PlaySE(157, 0x00, 0x64)
    FadeOut(300, 0, 100)
    TalkSetChrName('')
    SetMessageWindowPos(-1, -1, -1, -1)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '认证单元已经启动了……\n',
            '但这个地方好像没什么特别的反应。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Return,
        ),
        'loc_666',
    )

    ChrTalk(
        0x010A,
        (
            '#0120191470V#814F艾丝蒂尔。\n',
            '好像不是这里哦。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0120191471V先往前走吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ClearScenaFlags(ScenaFlag(0x0000, 0, 0x0))

    Jump('loc_892')

    def _loc_666(): pass

    label('loc_666')

    ExecExpressionWithReg(
        0x0002,
        (
            Expr.Rand,
            (Expr.PushLong, 0x8),
            Expr.Mod,
            Expr.Nop,
            Expr.Return,
        ),
    )

    If(
        (
            (Expr.PushReg, 0x2),
            (Expr.PushLong, 0x0),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_6B8',
    )

    ChrTalk(
        0x010A,
        (
            '#0120191472V#812F嗯～这里好像\n',
            '没什么可用的东西。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_88F')

    def _loc_6B8(): pass

    label('loc_6B8')

    If(
        (
            (Expr.PushReg, 0x2),
            (Expr.PushLong, 0x1),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_6FE',
    )

    ChrTalk(
        0x010A,
        (
            '#0120191473V#813F嗯～这里好像\n',
            '没什么可用的东西。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_88F')

    def _loc_6FE(): pass

    label('loc_6FE')

    If(
        (
            (Expr.PushReg, 0x2),
            (Expr.PushLong, 0x2),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_742',
    )

    ChrTalk(
        0x010A,
        (
            '#0120191474V#814F这里好像\n',
            '没什么可用的东西吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_88F')

    def _loc_742(): pass

    label('loc_742')

    If(
        (
            (Expr.PushReg, 0x2),
            (Expr.PushLong, 0x3),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_788',
    )

    ChrTalk(
        0x010A,
        (
            '#0120191475V#817F嗯～这里好像\n',
            '没什么可用的东西。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_88F')

    def _loc_788(): pass

    label('loc_788')

    If(
        (
            (Expr.PushReg, 0x2),
            (Expr.PushLong, 0x4),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_7CE',
    )

    ChrTalk(
        0x010A,
        (
            '#0120191476V#818F嗯～这里好像\n',
            '没什么可用的东西。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_88F')

    def _loc_7CE(): pass

    label('loc_7CE')

    If(
        (
            (Expr.PushReg, 0x2),
            (Expr.PushLong, 0x5),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_80C',
    )

    ChrTalk(
        0x010A,
        (
            '#0120191477V#819F嗯～看来\n',
            '没找对地方呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_88F')

    def _loc_80C(): pass

    label('loc_80C')

    If(
        (
            (Expr.PushReg, 0x2),
            (Expr.PushLong, 0x6),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_84F',
    )

    ChrTalk(
        0x010A,
        (
            '#0120191478V#1315F这里好像\n',
            '没什么可用的东西。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_88F')

    def _loc_84F(): pass

    label('loc_84F')

    If(
        (
            (Expr.PushReg, 0x2),
            (Expr.PushLong, 0x7),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_88F',
    )

    ChrTalk(
        0x010A,
        (
            '#0120191479V#1316F这里好像\n',
            '没什么可用的东西。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_88F(): pass

    label('loc_88F')

    SetScenaFlags(ScenaFlag(0x0000, 0, 0x0))

    def _loc_892(): pass

    label('loc_892')

    TalkEnd(0x00FF)

    def _loc_895(): pass

    label('loc_895')

    MapClearFlags(0x00000080)

    Return()

def main():
    scena.run(globals())

if __name__ == '__main__':
    Try(main)
