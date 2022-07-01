import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED62.Parser.scena_writer_helper import *
try:
    import C4200_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('C4200   ._SN')

stringTable = [
    TXT(0x00, '@FileName'),
    TXT(0x01, ''),
    TXT(0x02, ''),
    TXT(0x03, ''),
    TXT(0x04, ''),
    TXT(0x05, ''),
    TXT(0x06, ''),
    TXT(0x07, ''),
    TXT(0x08, ''),
    TXT(0x09, ''),
]

# id: 0xFFFF offset: 0x0
@scena.Header('Header')
def Header():
    header = ScenaHeader()
    header.mapName        = 'Grancel'
    header.mapModel       = 'C4200.x'
    header.mapIndex       = 1
    header.bgm            = 31
    header.flags          = 0x0000
    header.entryFunction  = 0xFFFF
    header.importTable    = [0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF]
    header.reserved       = 0
    return header

# id: 0xFFFF offset: 0x784
@scena.StringTable('StringTable')
def StringTable():
    return stringTable

# id: 0x10000 offset: 0x64
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

# id: 0x10001 offset: 0xA8
@scena.ChipData('ChipData')
def ChipData():
    return [
        # (ch, cp)
        ('ED6_DT09/CH10490._CH', 'ED6_DT09/CH10490P._CP'),
        ('ED6_DT09/CH10491._CH', 'ED6_DT09/CH10491P._CP'),
        ('ED6_DT09/CH10500._CH', 'ED6_DT09/CH10500P._CP'),
        ('ED6_DT09/CH10501._CH', 'ED6_DT09/CH10501P._CP'),
        ('ED6_DT09/CH10510._CH', 'ED6_DT09/CH10510P._CP'),
        ('ED6_DT09/CH10511._CH', 'ED6_DT09/CH10511P._CP'),
        ('ED6_DT09/CH11110._CH', 'ED6_DT09/CH11110P._CP'),
        ('ED6_DT09/CH11111._CH', 'ED6_DT09/CH11111P._CP'),
        ('ED6_DT09/CH11120._CH', 'ED6_DT09/CH11120P._CP'),
        ('ED6_DT09/CH11121._CH', 'ED6_DT09/CH11121P._CP'),
        ('ED6_DT09/CH11130._CH', 'ED6_DT09/CH11130P._CP'),
        ('ED6_DT09/CH11131._CH', 'ED6_DT09/CH11131P._CP'),
        ('ED6_DT09/CH11140._CH', 'ED6_DT09/CH11140P._CP'),
        ('ED6_DT09/CH11141._CH', 'ED6_DT09/CH11141P._CP'),
        ('ED6_DT09/CH11150._CH', 'ED6_DT09/CH11150P._CP'),
        ('ED6_DT09/CH11151._CH', 'ED6_DT09/CH11151P._CP'),
    ]

# id: 0x10002 offset: 0x12A
@scena.NpcData('NpcData')
def NpcData():
    return (
    )

# id: 0x10003 offset: 0x12A
@scena.MonsterData('MonsterData')
def MonsterData():
    return (
        ScenaMonsterData(
            x           = 1040,
            z           = 0,
            y           = 33740,
            word_0C     = 0x00B4,
            word_0E     = 0x0006,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x0271,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            x           = -13230,
            z           = 0,
            y           = 63010,
            word_0C     = 0x00B4,
            word_0E     = 0x0006,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x0271,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            x           = 24830,
            z           = 0,
            y           = 62910,
            word_0C     = 0x00B4,
            word_0E     = 0x0006,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x0271,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            x           = -71240,
            z           = 0,
            y           = 42750,
            word_0C     = 0x00B4,
            word_0E     = 0x0006,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x0271,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            x           = -75480,
            z           = 0,
            y           = -690,
            word_0C     = 0x00B4,
            word_0E     = 0x0006,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x0271,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            x           = -32930,
            z           = 0,
            y           = -57110,
            word_0C     = 0x00B4,
            word_0E     = 0x000A,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x0273,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            x           = 20530,
            z           = 0,
            y           = -113240,
            word_0C     = 0x00B4,
            word_0E     = 0x000A,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x0273,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            x           = 280,
            z           = 0,
            y           = -131490,
            word_0C     = 0x00B4,
            word_0E     = 0x000A,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x0273,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
    )

# id: 0x10004 offset: 0x20A
@scena.EventData('EventData')
def EventData():
    return (
    )

# id: 0x10005 offset: 0x20A
@scena.ActorData('ActorData')
def ActorData():
    return (
        ScenaActorData(
            triggerX            = -74020,
            triggerZ            = 0,
            triggerY            = -15990,
            triggerRange        = 1000,
            actorX              = -74020,
            actorZ              = 1500,
            actorY              = -16720,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0002,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = 12830,
            triggerZ            = 0,
            triggerY            = -124920,
            triggerRange        = 1000,
            actorX              = 13480,
            actorZ              = 1500,
            actorY              = -124890,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0003,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = 22010,
            triggerZ            = 0,
            triggerY            = -124520,
            triggerRange        = 1000,
            actorX              = 21700,
            actorZ              = 1500,
            actorY              = -125270,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0004,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = -11770,
            triggerZ            = 0,
            triggerY            = 4500,
            triggerRange        = 1000,
            actorX              = -11700,
            actorZ              = -1000,
            actorY              = 1260,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0005,
            word_22             = 0x0000,
        ),
    )

# id: 0x0000 offset: 0x29A
@scena.Code('PreInit')
def PreInit():
    Return()

# id: 0x0001 offset: 0x29B
@scena.Code('Init')
def Init():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02E2, 0, 0x1710)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_2AD',
    )

    OP_6F(0x0000, 0)

    Jump('loc_2B4')

    def _loc_2AD(): pass

    label('loc_2AD')

    OP_6F(0x0000, 60)

    def _loc_2B4(): pass

    label('loc_2B4')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02E2, 1, 0x1711)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_2C6',
    )

    OP_6F(0x0001, 0)

    Jump('loc_2CD')

    def _loc_2C6(): pass

    label('loc_2C6')

    OP_6F(0x0001, 60)

    def _loc_2CD(): pass

    label('loc_2CD')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02E2, 3, 0x1713)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_2DF',
    )

    OP_6F(0x0002, 0)

    Jump('loc_2E6')

    def _loc_2DF(): pass

    label('loc_2DF')

    OP_6F(0x0002, 60)

    def _loc_2E6(): pass

    label('loc_2E6')

    OP_E0(0x00, 0xDC, 0xDE, 0xFE, 0xFF, 0x00, 0x00, 0x00, 0x00, 0x96, 0xBF, 0xFF, 0xFF)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C7, 0, 0x1638)),
            (Expr.TestScenaFlags, ScenaFlag(0x02C7, 5, 0x163D)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_309',
    )

    OP_10(0x0F, 0x00)
    OP_10(0x10, 0x01)

    Jump('loc_30F')

    def _loc_309(): pass

    label('loc_309')

    OP_10(0x0F, 0x01)
    OP_10(0x10, 0x00)

    def _loc_30F(): pass

    label('loc_30F')

    OP_22(0x01CD, 0x01, 0x64)

    Return()

# id: 0x0002 offset: 0x315
@scena.Code('ReInit')
def ReInit():
    UnlockAchievement(0x02, 0xFD, 0x00, 0x00)
    SetMapFlags(0x08000000)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02E2, 0, 0x1710)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_3F2',
    )

    OP_22(0x002B, 0x00, 0x64)
    OP_70(0x0000, 0x0000003C)
    Sleep(500)

    If(
        (
            (Expr.Eval, "AddItem(ItemTable['不可思议的糊'], 1)"),
            Expr.Return,
        ),
        'loc_389',
    )

    FadeOut(300, 0, 100)
    OP_22(0x0011, 0x00, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '得到了',
            (TxtCtl.Item, ItemTable['不可思议的糊']),
            (TxtCtl.SetColor, 0x0),
            '。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)
    OP_A2(0x1710)

    Jump('loc_3EF')

    def _loc_389(): pass

    label('loc_389')

    FadeOut(300, 0, 100)
    SetChrName('')

    Talk(
        (
            '宝箱里装有',
            (TxtCtl.Item, ItemTable['不可思议的糊']),
            (TxtCtl.SetColor, 0x0),
            '。   \n',
            '所持物品已经满了，',
            (TxtCtl.Item, ItemTable['不可思议的糊']),
            (TxtCtl.SetColor, 0x0),
            '只能放弃了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    OP_22(0x002C, 0x00, 0x64)
    OP_6F(0x0000, 60)
    OP_70(0x0000, 0x00000000)

    def _loc_3EF(): pass

    label('loc_3EF')

    Jump('loc_423')

    def _loc_3F2(): pass

    label('loc_3F2')

    FadeOut(300, 0, 100)
    SetChrName('')

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
    def _loc_423(): pass

    label('loc_423')

    Sleep(30)

    TalkEnd(0x00FF)
    ClearMapFlags(0x08000000)

    Return()

# id: 0x0003 offset: 0x431
@scena.Code('func_03_431')
def func_03_431():
    UnlockAchievement(0x02, 0xFE, 0x00, 0x00)
    SetMapFlags(0x08000000)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02E2, 1, 0x1711)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_50E',
    )

    OP_22(0x002B, 0x00, 0x64)
    OP_70(0x0001, 0x0000003C)
    Sleep(500)

    If(
        (
            (Expr.Eval, "AddItem(ItemTable['火绒草铠甲'], 1)"),
            Expr.Return,
        ),
        'loc_4A5',
    )

    FadeOut(300, 0, 100)
    OP_22(0x0011, 0x00, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '得到了',
            (TxtCtl.Item, ItemTable['火绒草铠甲']),
            (TxtCtl.SetColor, 0x0),
            '。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)
    OP_A2(0x1711)

    Jump('loc_50B')

    def _loc_4A5(): pass

    label('loc_4A5')

    FadeOut(300, 0, 100)
    SetChrName('')

    Talk(
        (
            '宝箱里装有',
            (TxtCtl.Item, ItemTable['火绒草铠甲']),
            (TxtCtl.SetColor, 0x0),
            '。   \n',
            '所持物品已经满了，',
            (TxtCtl.Item, ItemTable['火绒草铠甲']),
            (TxtCtl.SetColor, 0x0),
            '只能放弃了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    OP_22(0x002C, 0x00, 0x64)
    OP_6F(0x0001, 60)
    OP_70(0x0001, 0x00000000)

    def _loc_50B(): pass

    label('loc_50B')

    Jump('loc_53F')

    def _loc_50E(): pass

    label('loc_50E')

    FadeOut(300, 0, 100)
    SetChrName('')

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
    def _loc_53F(): pass

    label('loc_53F')

    Sleep(30)

    TalkEnd(0x00FF)
    ClearMapFlags(0x08000000)

    Return()

# id: 0x0004 offset: 0x54D
@scena.Code('func_04_54D')
def func_04_54D():
    UnlockAchievement(0x02, 0xFF, 0x00, 0x00)
    SetMapFlags(0x08000000)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02E2, 3, 0x1713)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_62A',
    )

    OP_22(0x002B, 0x00, 0x64)
    OP_70(0x0002, 0x0000003C)
    Sleep(500)

    If(
        (
            (Expr.Eval, "AddItem(ItemTable['白银护腕'], 1)"),
            Expr.Return,
        ),
        'loc_5C1',
    )

    FadeOut(300, 0, 100)
    OP_22(0x0011, 0x00, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '得到了',
            (TxtCtl.Item, ItemTable['白银护腕']),
            (TxtCtl.SetColor, 0x0),
            '。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)
    OP_A2(0x1713)

    Jump('loc_627')

    def _loc_5C1(): pass

    label('loc_5C1')

    FadeOut(300, 0, 100)
    SetChrName('')

    Talk(
        (
            '宝箱里装有',
            (TxtCtl.Item, ItemTable['白银护腕']),
            (TxtCtl.SetColor, 0x0),
            '。   \n',
            '所持物品已经满了，',
            (TxtCtl.Item, ItemTable['白银护腕']),
            (TxtCtl.SetColor, 0x0),
            '只能放弃了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    OP_22(0x002C, 0x00, 0x64)
    OP_6F(0x0002, 60)
    OP_70(0x0002, 0x00000000)

    def _loc_627(): pass

    label('loc_627')

    Jump('loc_65B')

    def _loc_62A(): pass

    label('loc_62A')

    FadeOut(300, 0, 100)
    SetChrName('')

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
    def _loc_65B(): pass

    label('loc_65B')

    Sleep(30)

    TalkEnd(0x00FF)
    ClearMapFlags(0x08000000)

    Return()

# id: 0x0005 offset: 0x669
@scena.Code('func_05_669')
def func_05_669():
    EventBegin(0x01)

    ChrTalk(
        0x0101,
        (
            '#0011860001V#1001F这里好像可以钓上什么来。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_06A1')
    def lambda_06A1():
        OP_6D(-12420, 0, 1330, 1500)

        ExitThread()

    DispatchAsync(0x0000, 0x0001, lambda_06A1)

    @scena.Lambda('lambda_06B9')
    def lambda_06B9():
        OP_67(0, 9500, -10000, 1500)

        ExitThread()

    DispatchAsync(0x0000, 0x0002, lambda_06B9)

    @scena.Lambda('lambda_06D1')
    def lambda_06D1():
        OP_6B(2800, 1500)

        ExitThread()

    DispatchAsync(0x0001, 0x0001, lambda_06D1)

    @scena.Lambda('lambda_06E1')
    def lambda_06E1():
        OP_6C(45000, 1500)

        ExitThread()

    DispatchAsync(0x0001, 0x0002, lambda_06E1)

    Sleep(1000)

    SetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '钓鱼吗？',
            (TxtCtl.SetColor, 0x0),
            TxtCtl.Enter,
        ),
    )

    ExecExpressionWithVar(
        0x28,
        (
            (Expr.PushLong, 0x18),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Menu(
        0,
        10,
        32,
        1,
        (
            TXT(0x00, '钓鱼\n'),
            TXT(0x01, '离开\n'),
        ),
    )

    MenuEnd(0x0000)

    ExecExpressionWithVar(
        0x28,
        (
            (Expr.PushLong, 0xFFFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    OP_5F(0x0000)
    OP_56(0x00)
    WaitForThreadExit(0x0000, 0x0001)

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x0),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_768',
    )

    OP_C0(0x0E, 0x0000002A, 0xFFFFD1B6, 0x00000000, 0x00001194, 0x000000B4, 0xFFFFCC48, 0x00000000, 0xFFFFFE2A)
    OP_0D()
    EventEnd(0x01)

    Jump('loc_777')

    def _loc_768(): pass

    label('loc_768')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x0),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_777',
    )

    EventEnd(0x01)

    def _loc_777(): pass

    label('loc_777')

    Return()

def main():
    scena.run(globals())

if __name__ == '__main__':
    Try(main)
