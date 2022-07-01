import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED62.Parser.scena_writer_helper import *
try:
    import C4203_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('C4203   ._SN')

stringTable = [
    TXT(0x00, '@FileName'),
    TXT(0x01, ''),
    TXT(0x02, ''),
    TXT(0x03, ''),
    TXT(0x04, ''),
]

# id: 0xFFFF offset: 0x0
@scena.Header('Header')
def Header():
    header = ScenaHeader()
    header.mapName        = 'Grancel'
    header.mapModel       = 'C4203.x'
    header.mapIndex       = 1
    header.bgm            = 31
    header.flags          = 0x0000
    header.entryFunction  = 0xFFFF
    header.importTable    = [0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF]
    header.reserved       = 0
    return header

# id: 0xFFFF offset: 0x4C9
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
            x           = -47360,
            z           = 0,
            y           = 42620,
            word_0C     = 0x00B4,
            word_0E     = 0x000C,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x0274,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            x           = -121330,
            z           = 0,
            y           = 50600,
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
            x           = -88180,
            z           = 0,
            y           = 51510,
            word_0C     = 0x00B4,
            word_0E     = 0x0008,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x0272,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
    )

# id: 0x10004 offset: 0x17E
@scena.EventData('EventData')
def EventData():
    return (
    )

# id: 0x10005 offset: 0x17E
@scena.ActorData('ActorData')
def ActorData():
    return (
        ScenaActorData(
            triggerX            = -91330,
            triggerZ            = 0,
            triggerY            = 60050,
            triggerRange        = 1000,
            actorX              = -91210,
            actorZ              = 1500,
            actorY              = 60790,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0002,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = -55090,
            triggerZ            = 0,
            triggerY            = 90500,
            triggerRange        = 1000,
            actorX              = -55410,
            actorZ              = -500,
            actorY              = 85690,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0004,
            word_22             = 0x0000,
        ),
    )

# id: 0x0000 offset: 0x1C6
@scena.Code('PreInit')
def PreInit():
    Return()

# id: 0x0001 offset: 0x1C7
@scena.Code('Init')
def Init():
    OP_72(0x0000, 0x0010)
    OP_6F(0x0000, 240)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02E3, 7, 0x171F)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_1E5',
    )

    OP_6F(0x0001, 0)

    Jump('loc_1EC')

    def _loc_1E5(): pass

    label('loc_1E5')

    OP_6F(0x0001, 60)

    def _loc_1EC(): pass

    label('loc_1EC')

    OP_22(0x01CD, 0x01, 0x64)

    Return()

# id: 0x0002 offset: 0x1F2
@scena.Code('ReInit')
def ReInit():
    UnlockAchievement(0x02, 0x06, 0x01, 0x00)
    SetMapFlags(0x08000000)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02E3, 7, 0x171F)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_2CF',
    )

    OP_22(0x002B, 0x00, 0x64)
    OP_70(0x0001, 0x0000003C)
    Sleep(500)

    If(
        (
            (Expr.Eval, "AddItem(ItemTable['骨肉相连'], 1)"),
            Expr.Return,
        ),
        'loc_266',
    )

    FadeOut(300, 0, 100)
    OP_22(0x0011, 0x00, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '得到了',
            (TxtCtl.Item, ItemTable['骨肉相连']),
            (TxtCtl.SetColor, 0x0),
            '。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)
    OP_A2(0x171F)

    Jump('loc_2CC')

    def _loc_266(): pass

    label('loc_266')

    FadeOut(300, 0, 100)
    SetChrName('')

    Talk(
        (
            '宝箱里装有',
            (TxtCtl.Item, ItemTable['骨肉相连']),
            (TxtCtl.SetColor, 0x0),
            '。   \n',
            '所持物品已经满了，',
            (TxtCtl.Item, ItemTable['骨肉相连']),
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

    def _loc_2CC(): pass

    label('loc_2CC')

    Jump('loc_300')

    def _loc_2CF(): pass

    label('loc_2CF')

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
    def _loc_300(): pass

    label('loc_300')

    Sleep(30)

    TalkEnd(0x00FF)
    ClearMapFlags(0x08000000)

    Return()

# id: 0x0003 offset: 0x30E
@scena.Code('func_03_30E')
def func_03_30E():
    EventBegin(0x01)
    FadeOut(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '门紧紧地关着。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)
    OP_90(0x0000, 0, 0, 1500, 3000, 0x00)
    Sleep(50)

    EventEnd(0x04)

    Return()

# id: 0x0004 offset: 0x369
@scena.Code('func_04_369')
def func_04_369():
    EventBegin(0x01)

    ChrTalk(
        0x0101,
        (
            '#0011860001V#1001F这里好像可以钓上什么来。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_03A1')
    def lambda_03A1():
        OP_6D(-55290, 0, 87580, 1500)

        ExitThread()

    DispatchAsync(0x0000, 0x0001, lambda_03A1)

    @scena.Lambda('lambda_03B9')
    def lambda_03B9():
        OP_67(0, 9500, -10000, 1500)

        ExitThread()

    DispatchAsync(0x0000, 0x0002, lambda_03B9)

    @scena.Lambda('lambda_03D1')
    def lambda_03D1():
        OP_6B(2800, 1500)

        ExitThread()

    DispatchAsync(0x0001, 0x0001, lambda_03D1)

    @scena.Lambda('lambda_03E1')
    def lambda_03E1():
        OP_6C(45000, 1500)

        ExitThread()

    DispatchAsync(0x0001, 0x0002, lambda_03E1)

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
        'loc_468',
    )

    OP_C0(0x0E, 0x0000002B, 0xFFFF28CE, 0x00000000, 0x00016184, 0x000000B4, 0xFFFF278E, 0xFFFFFE0C, 0x00014EBA)
    OP_0D()
    EventEnd(0x01)

    Jump('loc_477')

    def _loc_468(): pass

    label('loc_468')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x0),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_477',
    )

    EventEnd(0x01)

    def _loc_477(): pass

    label('loc_477')

    Return()

# id: 0x0005 offset: 0x478
@scena.Code('func_05_478')
def func_05_478():
    FadeOut(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '机关门被封得很紧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)
    TalkEnd(0x00FF)

    Return()

def main():
    scena.run(globals())

if __name__ == '__main__':
    Try(main)
