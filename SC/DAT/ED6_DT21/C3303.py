import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED62.Parser.scena_writer_helper import *
try:
    import C3303_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('C3303   ._SN')

stringTable = [
    TXT(0x00, '@FileName'),
    TXT(0x01, '吉米'),
    TXT(0x02, '妖化企鹅'),
    TXT(0x03, '企鹅'),
    TXT(0x04, '企鹅'),
    TXT(0x05, '小企鹅'),
    TXT(0x06, '企鹅'),
    TXT(0x07, '企鹅'),
    TXT(0x08, '小企鹅'),
    TXT(0x09, '回音'),
    TXT(0x0A, ''),
]

# id: 0xFFFF offset: 0x0
@scena.Header('Header')
def Header():
    header = ScenaHeader()
    header.mapName        = 'Zeiss'
    header.mapModel       = 'C3303.x'
    header.mapIndex       = 1
    header.bgm            = 32
    header.flags          = 0x0000
    header.entryFunction  = 0xFFFF
    header.importTable    = [0xFFFFFFFF, 'ED6_DT21/C3303_1._SN', 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 'ED6_DT21/SUB000._SN', 0xFFFFFFFF]
    header.reserved       = 0
    return header

# id: 0xFFFF offset: 0x3F7
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
        ('ED6_DT07/CH01040._CH', 'ED6_DT07/CH01040P._CP'),
        ('ED6_DT29/CH12930._CH', 'ED6_DT29/CH12930P._CP'),
        ('ED6_DT09/CH10630._CH', 'ED6_DT09/CH10630P._CP'),
        ('ED6_DT09/CH10640._CH', 'ED6_DT09/CH10640P._CP'),
        ('ED6_DT09/CH10650._CH', 'ED6_DT09/CH10650P._CP'),
        ('ED6_DT09/CH10660._CH', 'ED6_DT09/CH10660P._CP'),
        ('ED6_DT09/CH10670._CH', 'ED6_DT09/CH10670P._CP'),
        ('ED6_DT09/CH10690._CH', 'ED6_DT09/CH10690P._CP'),
        ('ED6_DT27/CH04000._CH', 'ED6_DT27/CH04000P._CP'),
        ('ED6_DT27/CH04001._CH', 'ED6_DT27/CH04001P._CP'),
        ('ED6_DT07/CH00120._CH', 'ED6_DT07/CH00120P._CP'),
        ('ED6_DT07/CH00121._CH', 'ED6_DT07/CH00121P._CP'),
        ('ED6_DT06/CH20137._CH', 'ED6_DT06/CH20137P._CP'),
        ('ED6_DT07/CH00151._CH', 'ED6_DT07/CH00151P._CP'),
        ('ED6_DT07/CH00130._CH', 'ED6_DT07/CH00130P._CP'),
        ('ED6_DT07/CH00131._CH', 'ED6_DT07/CH00131P._CP'),
        ('ED6_DT07/CH00140._CH', 'ED6_DT07/CH00140P._CP'),
        ('ED6_DT07/CH00141._CH', 'ED6_DT07/CH00141P._CP'),
        ('ED6_DT07/CH00160._CH', 'ED6_DT07/CH00160P._CP'),
        ('ED6_DT07/CH00161._CH', 'ED6_DT07/CH00161P._CP'),
        ('ED6_DT07/CH00170._CH', 'ED6_DT07/CH00170P._CP'),
        ('ED6_DT07/CH00171._CH', 'ED6_DT07/CH00171P._CP'),
        ('ED6_DT27/CH03005._CH', 'ED6_DT27/CH03005P._CP'),
        ('ED6_DT26/CH20311._CH', 'ED6_DT26/CH20311P._CP'),
        ('ED6_DT29/CH12932._CH', 'ED6_DT29/CH12932P._CP'),
    ]

# id: 0x10002 offset: 0x172
@scena.NpcData('NpcData')
def NpcData():
    return (
        ScenaNpcData(
            x                   = 9460,
            z                   = 40,
            y                   = 112430,
            direction           = 90,
            word_0E             = 0,
            dword_10            = 0,
            chipIndex           = 0,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            x                   = 8000,
            z                   = -3500,
            y                   = 119800,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 1,
            chipIndex           = 1,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 5,
            chipIndex           = 5,
            npcIndex            = 0x01C1,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 6,
            chipIndex           = 6,
            npcIndex            = 0x01C1,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 7,
            chipIndex           = 7,
            npcIndex            = 0x01C1,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 5,
            chipIndex           = 5,
            npcIndex            = 0x01C1,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 6,
            chipIndex           = 6,
            npcIndex            = 0x01C1,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 7,
            chipIndex           = 7,
            npcIndex            = 0x01C1,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 0,
            chipIndex           = 0,
            npcIndex            = 0x01C1,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
    )

# id: 0x10003 offset: 0x292
@scena.MonsterData('MonsterData')
def MonsterData():
    return (
    )

# id: 0x10004 offset: 0x292
@scena.EventData('EventData')
def EventData():
    return (
        ScenaEventData(
            x           = 12660,
            y           = -2000,
            z           = 95880,
            range       = 3560,
            dword_10    = 0x000007D0,
            dword_14    = 0x0001848E,
            dword_18    = 0x00010000,
            dword_1C    = 0x00000000,
        ),
    )

# id: 0x10005 offset: 0x2B2
@scena.ActorData('ActorData')
def ActorData():
    return (
        ScenaActorData(
            triggerX            = 5350,
            triggerZ            = 50,
            triggerY            = 109980,
            triggerRange        = 1000,
            actorX              = 1170,
            actorZ              = -2060,
            actorY              = 108860,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0002,
            word_22             = 0x0000,
        ),
    )

# id: 0x0000 offset: 0x2D6
@scena.Code('PreInit')
def PreInit():
    Return()

# id: 0x0001 offset: 0x2D7
@scena.Code('Init')
def Init():
    OP_71(0x0000, 0x0004)
    OP_22(0x01CD, 0x01, 0x64)

    Return()

# id: 0x0002 offset: 0x2E2
@scena.Code('ReInit')
def ReInit():
    EventBegin(0x01)

    ChrTalk(
        0x0101,
        (
            '#0011860001V#1001F这里好像可以钓上什么来。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_031A')
    def lambda_031A():
        OP_6D(3000, 20, 108970, 1500)

        ExitThread()

    DispatchAsync(0x0000, 0x0001, lambda_031A)

    @scena.Lambda('lambda_0332')
    def lambda_0332():
        OP_67(0, 8000, -10000, 1500)

        ExitThread()

    DispatchAsync(0x0000, 0x0002, lambda_0332)

    @scena.Lambda('lambda_034A')
    def lambda_034A():
        OP_6B(3200, 1500)

        ExitThread()

    DispatchAsync(0x0001, 0x0001, lambda_034A)

    @scena.Lambda('lambda_035A')
    def lambda_035A():
        OP_6C(45000, 1500)

        ExitThread()

    DispatchAsync(0x0001, 0x0002, lambda_035A)

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
        'loc_3E1',
    )

    OP_C0(0x0E, 0x00000020, 0x000014E6, 0x00000032, 0x0001AD9C, 0x0000010E, 0x0000078A, 0xFFFFFC18, 0x0001A928)
    OP_0D()
    EventEnd(0x01)

    Jump('loc_3F0')

    def _loc_3E1(): pass

    label('loc_3E1')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x0),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_3F0',
    )

    EventEnd(0x01)

    def _loc_3F0(): pass

    label('loc_3F0')

    Return()

def main():
    scena.run(globals())

if __name__ == '__main__':
    Try(main)
